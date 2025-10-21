import pytest
from io import BytesIO
from flask import make_response
from python.prohibition_web_svc.middleware import files_middleware

class FakeMinioObject:
    def __init__(self, data=b"fake data"):
        self.data = data
        self._closed = False

    def stream(self, chunk_size):
        for i in range(0, len(self.data), chunk_size):
            yield self.data[i:i+chunk_size]

    def close(self):
        self._closed = True

    def release_conn(self):
        pass


@pytest.fixture
def fake_file():
    class File:
        filename = "test.pdf"

        def read(self):
            return b"dummy content"
    return File()


def test_upload_file_success(monkeypatch, fake_file):
    # Patch Minio put_object to simulate success
    def fake_put_object(bucket, object_name, stream, length):
        return None
    monkeypatch.setattr(files_middleware.minio_client, "put_object", fake_put_object)

    kwargs = {"request": type("Req", (), {"files": {"file": fake_file}, "form": {}})()}
    flag, result = files_middleware.upload_file(**kwargs)

    assert flag is True
    assert result["status"] == 201
    assert b"uploaded successfully" in result["response"].data


def test_upload_file_no_file():
    kwargs = {"request": type("Req", (), {"files": {}, "form": {}})()}
    flag, result = files_middleware.upload_file(**kwargs)
    assert flag is False
    assert result["response"].status_code == 400


def test_get_file_stream_success(monkeypatch):
    # Patch Minio get_object
    monkeypatch.setattr(files_middleware.minio_client, "get_object", lambda bucket, filename: FakeMinioObject(b"abc"))

    kwargs = {"filename": "file.pdf"}
    flag, result = files_middleware.get_file_stream(**kwargs)
    assert flag is True
    assert result["status"] == 200
    data = b"".join(result["response"].response)
    assert data == b"abc"


def test_get_file_stream_not_found(monkeypatch):
    from minio.error import S3Error
    def fake_get_object(bucket, filename):
        raise S3Error("NoSuchKey", "Object does not exist", bucket, filename, None, None)
    monkeypatch.setattr(files_middleware.minio_client, "get_object", fake_get_object)

    kwargs = {"filename": "missing.pdf"}
    flag, result = files_middleware.get_file_stream(**kwargs)
    assert flag is False
    assert result["status"] == 404


def test_generate_presigned_url_success(monkeypatch):
    monkeypatch.setattr(files_middleware.minio_client, "stat_object", lambda bucket, filename: None)
    monkeypatch.setattr(files_middleware.minio_client, "presigned_get_object", lambda bucket, filename, expires: "http://fake.url")

    kwargs = {}
    flag, result = files_middleware.generate_presigned_url("file.pdf", 3600, **kwargs)
    assert flag is True
    assert result["status"] == 200
    assert result["response"].json["url"] == "http://fake.url"


def test_generate_presigned_url_not_found(monkeypatch):
    from minio.error import S3Error
    def fake_stat(bucket, filename):
        raise S3Error("NoSuchKey", "Object does not exist", bucket, filename, None, None)
    monkeypatch.setattr(files_middleware.minio_client, "stat_object", fake_stat)

    flag, result = files_middleware.generate_presigned_url("missing.pdf")
    assert flag is False
    assert result["status"] == 404


def test_list_files_success(monkeypatch):
    class Obj:
        object_name = "file.pdf"
        size = 123
        last_modified = None

    monkeypatch.setattr(files_middleware.minio_client, "list_objects", lambda bucket, prefix, recursive: [Obj()])
    flag, result = files_middleware.list_files(prefix="")
    assert flag is True
    assert result["status"] == 200
    assert result["response"].json["items"][0]["object_name"] == "file.pdf"


def test_delete_file_success(monkeypatch):
    monkeypatch.setattr(files_middleware.minio_client, "stat_object", lambda bucket, filename: None)
    monkeypatch.setattr(files_middleware.minio_client, "remove_object", lambda bucket, filename: None)

    flag, result = files_middleware.delete_file(filename="file.pdf")
    assert flag is True
    assert result["status"] == 200
    assert "deleted successfully" in result["response"].data.decode()


def test_delete_file_not_found(monkeypatch):
    from minio.error import S3Error
    def fake_stat(bucket, filename):
        raise S3Error("NoSuchKey", "Object does not exist", bucket, filename, None, None)
    monkeypatch.setattr(files_middleware.minio_client, "stat_object", fake_stat)

    flag, result = files_middleware.delete_file(filename="missing.pdf")
    assert flag is False
    assert result["status"] == 404
    assert "not found" in result["response"].data.decode()
