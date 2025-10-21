import pytest
from unittest.mock import patch, MagicMock
from io import BytesIO
from flask import Flask

from python.prohibition_web_svc.middleware import files_middleware


@pytest.fixture
def app():
    """Flask app fixture to provide app context for tests."""
    app = Flask(__name__)
    with app.app_context():
        yield app


class MockRequest:
    """Mock request object with files and form data."""
    def __init__(self, files=None, form=None):
        self.files = files or {}
        self.form = form or {}


class MockFile:
    """Mock uploaded file object."""
    def __init__(self, filename, data):
        self.filename = filename
        self._data = data

    def read(self):
        return self._data


def make_fake_s3_error(code="NoSuchKey"):
    from minio.error import S3Error
    err = S3Error(resource="/bucket/file.pdf", request_id="123", host_id="abc", response="NotFound")
    err.code = code
    return err


def test_upload_file_success(app):
    file_data = b"Hello World"
    request = MockRequest(files={"file": MockFile("test.txt", file_data)})
    kwargs = {"request": request}

    with patch.object(files_middleware.minio_client, "put_object") as mock_put:
        flag, result = files_middleware.upload_file(**kwargs)

    assert flag is True
    assert result["status"] == 201
    assert b"uploaded successfully" in result["response"].data
    mock_put.assert_called_once()


def test_upload_file_no_file(app):
    request = MockRequest()
    kwargs = {"request": request}
    flag, result = files_middleware.upload_file(**kwargs)

    assert flag is False
    assert result["status"] == 400
    assert b"No file uploaded" in result["response"].data


def test_get_file_stream_success(app):
    kwargs = {"filename": "test.txt"}
    fake_stream = MagicMock()
    fake_stream.stream = MagicMock(return_value=[b"chunk1", b"chunk2"])
    fake_stream.close = MagicMock()
    fake_stream.release_conn = MagicMock()

    with patch.object(files_middleware.minio_client, "get_object", return_value=fake_stream):
        flag, result = files_middleware.get_file_stream(**kwargs)

    assert flag is True
    assert result["status"] == 200
    assert "Content-Disposition" in result["response"].headers


def test_get_file_stream_not_found(app):
    kwargs = {"filename": "missing.txt"}
    fake_error = make_fake_s3_error()

    with patch.object(files_middleware.minio_client, "get_object", side_effect=fake_error):
        flag, result = files_middleware.get_file_stream(**kwargs)

    assert flag is False
    assert result["status"] == 404
    assert b"Not found" in result["response"].data


def test_generate_presigned_url_success(app):
    kwargs = {}
    with patch.object(files_middleware.minio_client, "stat_object", return_value=True):
        with patch.object(files_middleware.minio_client, "presigned_get_object", return_value="http://fake-url"):
            flag, result = files_middleware.generate_presigned_url("file.txt", expiry=3600, **kwargs)

    assert flag is True
    assert result["status"] == 200
    assert b"http://fake-url" in result["response"].data


def test_generate_presigned_url_not_found(app):
    kwargs = {}
    fake_error = make_fake_s3_error()

    with patch.object(files_middleware.minio_client, "stat_object", side_effect=fake_error):
        flag, result = files_middleware.generate_presigned_url("missing.txt", **kwargs)

    assert flag is False
    assert result["status"] == 404
    assert b"File not found" in result["response"].data


def test_list_files_success(app):
    class FakeObject:
        def __init__(self, name, size, last_modified):
            self.object_name = name
            self.size = size
            self.last_modified = last_modified

    from datetime import datetime
    fake_objects = [
        FakeObject("file1.txt", 123, datetime.utcnow()),
        FakeObject("file2.txt", 456, datetime.utcnow())
    ]

    with patch.object(files_middleware.minio_client, "list_objects", return_value=fake_objects):
        flag, result = files_middleware.list_files(prefix="")

    assert flag is True
    assert result["status"] == 200
    assert b"file1.txt" in result["response"].data
    assert b"file2.txt" in result["response"].data


def test_delete_file_success(app):
    kwargs = {"filename": "file.txt"}
    with patch.object(files_middleware.minio_client, "stat_object", return_value=True):
        with patch.object(files_middleware.minio_client, "remove_object", return_value=True) as mock_remove:
            flag, result = files_middleware.delete_file(**kwargs)

    assert flag is True
    assert result["status"] == 200
    assert b"deleted successfully" in result["response"].data
    mock_remove.assert_called_once()


def test_delete_file_not_found(app):
    kwargs = {"filename": "missing.txt"}
    fake_error = make_fake_s3_error()
    fake_error.code = "NoSuchKey"

    with patch.object(files_middleware.minio_client, "stat_object", side_effect=fake_error):
        flag, result = files_middleware.delete_file(**kwargs)

    assert flag is False
    assert result["status"] == 404
    assert b"not found" in result["response"].data
