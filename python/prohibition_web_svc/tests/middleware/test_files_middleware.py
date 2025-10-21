import pytest
from flask import Flask
from io import BytesIO
from unittest.mock import patch, MagicMock
from python.prohibition_web_svc.middleware import files_middleware

# Mock request object
class MockRequest:
    def __init__(self, files=None, form=None):
        self.files = files or {}
        self.form = form or {}

@pytest.fixture
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

@pytest.fixture
def fake_file():
    class File:
        filename = "test.pdf"
        def read(self):
            return b"dummy content"
    return File()

def test_upload_file_success(app, fake_file):
    request = MockRequest(files={"file": fake_file})
    kwargs = {"request": request}

    with patch.object(files_middleware.minio_client, "put_object", return_value=None):
        flag, result = files_middleware.upload_file(**kwargs)

    assert flag is True
    assert result["status"] == 201
    assert b"uploaded successfully" in result["response"].data

def test_upload_file_no_file(app):
    request = MockRequest(files={})
    kwargs = {"request": request}
    flag, result = files_middleware.upload_file(**kwargs)
    assert flag is False
    assert result["response"].status_code == 400

def test_get_file_stream_success(app):
    class FakeObject:
        def stream(self, chunk_size):
            yield b"abc"
        def close(self): pass
        def release_conn(self): pass

    kwargs = {"filename": "file.pdf"}
    with patch.object(files_middleware.minio_client, "get_object", return_value=FakeObject()):
        flag, result = files_middleware.get_file_stream(**kwargs)

    assert flag is True
    assert result["status"] == 200
    assert b"abc" in b"".join(result["response"].response)

def test_get_file_stream_not_found(app):
    kwargs = {"filename": "file.pdf"}
    with patch.object(files_middleware.minio_client, "get_object", side_effect=files_middleware.S3Error("NoSuchKey", "Not found")):
        flag, result = files_middleware.get_file_stream(**kwargs)

    assert flag is False
    assert result["status"] == 404

def test_generate_presigned_url_success(app):
    filename = "file.pdf"
    with patch.object(files_middleware.minio_client, "stat_object", return_value=None), \
         patch.object(files_middleware.minio_client, "presigned_get_object", return_value="http://example.com/url"):
        flag, result = files_middleware.generate_presigned_url(filename, expiry=3600)

    assert flag is True
    assert result["status"] == 200
    assert result["response"].json["url"] == "http://example.com/url"

def test_generate_presigned_url_not_found(app):
    filename = "file.pdf"
    with patch.object(files_middleware.minio_client, "stat_object", side_effect=files_middleware.S3Error("NoSuchKey", "Not found")):
        flag, result = files_middleware.generate_presigned_url(filename, expiry=3600)

    assert flag is False
    assert result["status"] == 404

def test_list_files_success(app):
    class FakeObject:
        object_name = "file1.pdf"
        size = 123
        last_modified = None

    with patch.object(files_middleware.minio_client, "list_objects", return_value=[FakeObject()]):
        flag, result = files_middleware.list_files(prefix="")

    assert flag is True
    assert result["status"] == 200
    assert "items" in result["response"].json

def test_delete_file_success(app):
    filename = "file.pdf"
    with patch.object(files_middleware.minio_client, "stat_object", return_value=None), \
         patch.object(files_middleware.minio_client, "remove_object", return_value=None):
        flag, result = files_middleware.delete_file(filename=filename)

    assert flag is True
    assert result["status"] == 200
    assert b"deleted successfully" in result["response"].data

def test_delete_file_not_found(app):
    filename = "file.pdf"
    e = files_middleware.S3Error("NoSuchKey", "Not found")
    e.code = "NoSuchKey"
    with patch.object(files_middleware.minio_client, "stat_object", side_effect=e):
        flag, result = files_middleware.delete_file(filename=filename)

    assert flag is False
    assert result["status"] == 404
