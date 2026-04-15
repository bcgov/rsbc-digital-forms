from __future__ import annotations

from datetime import datetime
from unittest.mock import MagicMock, patch, call

import pytest

from python.data_cleanup_job import data_cleanup_service as service


class TestCountPostgresRecords:
    def test_returns_correct_count(self):
        conn = MagicMock()
        cursor = MagicMock()
        cursor.fetchone.return_value = (42,)

        cursor_cm = MagicMock()
        cursor_cm.__enter__.return_value = cursor
        conn.cursor.return_value = cursor_cm

        cutoff = datetime(2025, 12, 1)
        count = service._count_postgres_records(conn, "df_errors", "received_dt", cutoff)

        assert count == 42
        cursor.execute.assert_called_once()
        query, params = cursor.execute.call_args.args
        assert "df_errors" in query
        assert "received_dt" in query
        assert params == (cutoff,)


class TestDeletePostgresRecords:
    def test_deletes_and_commits(self):
        conn = MagicMock()
        cursor = MagicMock()
        cursor.rowcount = 10

        cursor_cm = MagicMock()
        cursor_cm.__enter__.return_value = cursor
        conn.cursor.return_value = cursor_cm

        cutoff = datetime(2025, 12, 1)
        deleted = service._delete_postgres_records(conn, "event", "created_dt", cutoff)

        assert deleted == 10
        conn.commit.assert_called_once()
        query, params = cursor.execute.call_args.args
        assert "DELETE" in query
        assert "event" in query
        assert "created_dt" in query
        assert params == (cutoff,)


class TestCleanupPostgres:
    def test_dry_run_counts_without_deleting(self, monkeypatch):
        conn = MagicMock()
        conn_cm = MagicMock()
        conn_cm.__enter__.return_value = conn

        connect_mock = MagicMock(return_value=conn_cm)
        monkeypatch.setattr(service.psycopg2, "connect", connect_mock)

        count_mock = MagicMock(return_value=5)
        delete_mock = MagicMock()
        monkeypatch.setattr(service, "_count_postgres_records", count_mock)
        monkeypatch.setattr(service, "_delete_postgres_records", delete_mock)

        cutoff = datetime(2025, 12, 1)
        results = service.cleanup_postgres_DF(cutoff, dry_run=True)

        assert results == {"df_errors": 5}
        assert count_mock.call_count == 1
        delete_mock.assert_not_called()

    def test_live_mode_counts_and_deletes(self, monkeypatch):
        conn = MagicMock()
        conn_cm = MagicMock()
        conn_cm.__enter__.return_value = conn

        connect_mock = MagicMock(return_value=conn_cm)
        monkeypatch.setattr(service.psycopg2, "connect", connect_mock)

        count_mock = MagicMock(return_value=3)
        delete_mock = MagicMock(return_value=3)
        monkeypatch.setattr(service, "_count_postgres_records", count_mock)
        monkeypatch.setattr(service, "_delete_postgres_records", delete_mock)

        cutoff = datetime(2025, 12, 1)
        results = service.cleanup_postgres_DF(cutoff, dry_run=False)

        assert results == {"df_errors": 3}
        assert count_mock.call_count == 1
        assert delete_mock.call_count == 1

    def test_live_mode_skips_delete_when_count_is_zero(self, monkeypatch):
        conn = MagicMock()
        conn_cm = MagicMock()
        conn_cm.__enter__.return_value = conn

        connect_mock = MagicMock(return_value=conn_cm)
        monkeypatch.setattr(service.psycopg2, "connect", connect_mock)

        count_mock = MagicMock(return_value=0)
        delete_mock = MagicMock()
        monkeypatch.setattr(service, "_count_postgres_records", count_mock)
        monkeypatch.setattr(service, "_delete_postgres_records", delete_mock)

        cutoff = datetime(2025, 12, 1)
        service.cleanup_postgres_DF(cutoff, dry_run=False)

        delete_mock.assert_not_called()


class TestCleanupMongo:
    def test_dry_run_counts_without_deleting(self, monkeypatch):
        collection = MagicMock()
        collection.count_documents.return_value = 15

        db = MagicMock()
        db.__getitem__.return_value = collection

        client = MagicMock()
        client.__getitem__.return_value = db

        mongo_client_mock = MagicMock(return_value=client)
        monkeypatch.setattr(service, "MongoClient", mongo_client_mock)

        cutoff = datetime(2025, 12, 1)
        count = service.cleanup_mongo(cutoff, dry_run=True)

        assert count == 15
        collection.count_documents.assert_called_once_with({"created": {"$lt": cutoff}})
        collection.delete_many.assert_not_called()
        client.close.assert_called_once()

    def test_live_mode_counts_and_deletes(self, monkeypatch):
        delete_result = MagicMock()
        delete_result.deleted_count = 15

        collection = MagicMock()
        collection.count_documents.return_value = 15
        collection.delete_many.return_value = delete_result

        db = MagicMock()
        db.__getitem__.return_value = collection

        client = MagicMock()
        client.__getitem__.return_value = db

        mongo_client_mock = MagicMock(return_value=client)
        monkeypatch.setattr(service, "MongoClient", mongo_client_mock)

        cutoff = datetime(2025, 12, 1)
        count = service.cleanup_mongo(cutoff, dry_run=False)

        assert count == 15
        collection.delete_many.assert_called_once_with({"created": {"$lt": cutoff}})
        client.close.assert_called_once()

    def test_live_mode_skips_delete_when_count_is_zero(self, monkeypatch):
        collection = MagicMock()
        collection.count_documents.return_value = 0

        db = MagicMock()
        db.__getitem__.return_value = collection

        client = MagicMock()
        client.__getitem__.return_value = db

        mongo_client_mock = MagicMock(return_value=client)
        monkeypatch.setattr(service, "MongoClient", mongo_client_mock)

        cutoff = datetime(2025, 12, 1)
        count = service.cleanup_mongo(cutoff, dry_run=False)

        assert count == 0
        collection.delete_many.assert_not_called()
        client.close.assert_called_once()


class TestRunCleanup:
    def test_orchestrates_postgres_and_mongo_cleanup(self, monkeypatch):
        postgres_mock = MagicMock(return_value={"df_errors": 1})
        mongo_mock = MagicMock(return_value=5)
        monkeypatch.setattr(service, "cleanup_postgres_DF", postgres_mock)
        monkeypatch.setattr(service, "cleanup_mongo", mongo_mock)

        cutoff = datetime(2025, 12, 1)
        service.run_cleanup(cutoff, dry_run=True)

        postgres_mock.assert_called_once_with(cutoff, True)
        mongo_mock.assert_called_once_with(cutoff, True)
