import pytest
from io import BytesIO
from minio.error import S3Error
from unittest.mock import patch, MagicMock

from flask import Flask, Response, jsonify

from python.prohibition_web_svc.middleware import files_middleware

# ---------- Mock Request ----------
class MockRequest:
    def __init__(self, files=None, form=None):
        self.files = files or {}
        self.form = form or {}

# ---------- Helper for fake S3Error ----------
from minio.error import S3Error

def make_fake_s3_error(code="NoSuchKey", message="Object does not exist"):
    # S3Error(resource, request_id, host_id, code, message, response)
    return S3Error(resource="mock_resource",
                   request_id="mock_request",
                   host_id="mock_host",
                   code=code,
                   message=message,
                   response=None)

# ---------- Pytest fixtures ----------
@pytest.fixture
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

# ---------- Tests ----------

def test_upload_file_success(app):
    mock_file = MagicMock()
    mock_file.read.return_value = b"data"
    request = MockRequest(files={"file": mock_file}, form={"object_name": "test.txt"})
    kwargs = {"request": request}

    with patch.object(files_middleware.minio_client, "put_object", return_value=True):
        flag, result = files_middleware.upload_file(**kwargs)

    assert flag is True
    assert result["status"] == 201
    assert b"uploaded successfully" in result["response"].data


def test_upload_file_no_file(app):
    request = MockRequest()
    kwargs = {"request": request}

    flag, result = files_middleware.upload_file(**kwargs)

    assert flag is False
    assert result["status"] == 400
    assert b"No file uploaded" in result["response"].data


def test_get_file_stream_success(app):
    fake_obj = MagicMock()
    fake_obj.stream.return_value = [b"chunk1", b"chunk2"]
    request = MockRequest()
    kwargs = {"filename": "file.txt", "request": request}

    with patch.object(files_middleware.minio_client, "get_object", return_value=fake_obj):
        flag, result = files_middleware.get_file_stream(**kwargs)

    assert flag is True
    assert result["status"] == 200
    assert isinstance(result["response"], Response)
    content = b"".join(result["response"].response)
    assert content == b"chunk1chunk2"


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
    fake_url = "https://mocked-presigned-url.test/file.txt"
    with patch.object(files_middleware.minio_client, "stat_object", return_value=True), \
         patch.object(files_middleware.minio_client, "presigned_get_object", return_value=fake_url):
        flag, result = files_middleware.generate_presigned_url("file.txt", expiry=600, **kwargs)

    assert flag is True
    assert result["status"] == 200
    assert fake_url.encode() in result["response"].data


def test_generate_presigned_url_not_found(app):
    kwargs = {}
    fake_error = make_fake_s3_error()

    with patch.object(files_middleware.minio_client, "stat_object", side_effect=fake_error):
        flag, result = files_middleware.generate_presigned_url("missing.txt", **kwargs)

    assert flag is False
    assert result["status"] == 404
    assert b"File not found" in result["response"].data


def test_list_files_success(app):
    fake_obj = MagicMock()
    fake_obj.object_name = "file.txt"
    fake_obj.size = 123
    fake_obj.last_modified = None
    kwargs = {"prefix": ""}

    with patch.object(files_middleware.minio_client, "list_objects", return_value=[fake_obj]):
        flag, result = files_middleware.list_files(**kwargs)

    assert flag is True
    assert result["status"] == 200
    data = result["response"].get_json()
    assert data["items"][0]["object_name"] == "file.txt"


def test_delete_file_success(app):
    kwargs = {"filename": "file.txt"}

    with patch.object(files_middleware.minio_client, "stat_object", return_value=True), \
         patch.object(files_middleware.minio_client, "remove_object", return_value=True):
        flag, result = files_middleware.delete_file(**kwargs)

    assert flag is True
    assert result["status"] == 200
    assert b"deleted successfully" in result["response"].data


def test_delete_file_not_found(app):
    kwargs = {"filename": "missing.txt"}
    fake_error = make_fake_s3_error(code="NoSuchKey")

    with patch.object(files_middleware.minio_client, "stat_object", side_effect=fake_error):
        flag, result = files_middleware.delete_file(**kwargs)

    assert flag is False
    assert result["status"] == 404
    assert b"not found" in result["response"].data

# ---------- Additional negative tests for full coverage ----------

# ---------- Helper for generic Exception ----------
class DummyException(Exception):
    pass

# ---------- UPLOAD FILE EXCEPTIONS ----------
def test_upload_file_s3error(app):
    mock_file = MagicMock()
    mock_file.read.return_value = b"data"
    request = MagicMock()
    request.files = {"file": mock_file}
    request.form = {"object_name": "file.txt"}
    kwargs = {"request": request}
    
    fake_error = S3Error("res", "req", "host", "SomeCode", "SomeMessage", None)

    with patch.object(files_middleware.minio_client, "put_object", side_effect=fake_error):
        flag, result = files_middleware.upload_file(**kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"Failed to upload file" in result["response"].data


def test_upload_file_generic_exception(app):
    mock_file = MagicMock()
    mock_file.read.side_effect = DummyException("Oops")
    request = MagicMock()
    request.files = {"file": mock_file}
    kwargs = {"request": request}

    flag, result = files_middleware.upload_file(**kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"Internal server error" in result["response"].data


# ---------- GET FILE STREAM GENERIC EXCEPTION ----------
def test_get_file_stream_generic_exception(app):
    kwargs = {"filename": "file.txt"}
    with patch.object(files_middleware.minio_client, "get_object", side_effect=DummyException("Boom")):
        flag, result = files_middleware.get_file_stream(**kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"Internal server error" in result["response"].data


# ---------- GENERATE PRESIGNED URL S3ERROR ----------
def test_generate_presigned_url_s3error(app):
    kwargs = {}
    with patch.object(files_middleware.minio_client, "stat_object", return_value=True), \
         patch.object(files_middleware.minio_client, "presigned_get_object", side_effect=S3Error("r", "r", "h", "code", "msg", None)):

        flag, result = files_middleware.generate_presigned_url("file.txt", **kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"Unable to generate presigned URL" in result["response"].data


def test_generate_presigned_url_generic_exception(app):
    kwargs = {}
    with patch.object(files_middleware.minio_client, "stat_object", return_value=True), \
         patch.object(files_middleware.minio_client, "presigned_get_object", side_effect=DummyException("Boom")):

        flag, result = files_middleware.generate_presigned_url("file.txt", **kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"Internal server error" in result["response"].data


# ---------- LIST FILES EXCEPTIONS ----------
def test_list_files_s3error(app):
    kwargs = {}
    with patch.object(files_middleware.minio_client, "list_objects", side_effect=S3Error("r","r","h","code","msg",None)):
        flag, result = files_middleware.list_files(**kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"Unable to list files" in result["response"].data


def test_list_files_generic_exception(app):
    kwargs = {}
    with patch.object(files_middleware.minio_client, "list_objects", side_effect=DummyException("Boom")):
        flag, result = files_middleware.list_files(**kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"Internal server error" in result["response"].data


# ---------- DELETE FILE EXCEPTIONS ----------
def test_delete_file_generic_s3error(app):
    kwargs = {"filename": "file.txt"}
    fake_error = S3Error("r","r","h","SomeCode","SomeMessage",None)

    with patch.object(files_middleware.minio_client, "stat_object", return_value=True), \
         patch.object(files_middleware.minio_client, "remove_object", side_effect=fake_error):
        flag, result = files_middleware.delete_file(**kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"S3 operation failed" in result["response"].data


def test_delete_file_generic_exception(app):
    kwargs = {"filename": "file.txt"}
    with patch.object(files_middleware.minio_client, "stat_object", side_effect=DummyException("Boom")):
        flag, result = files_middleware.delete_file(**kwargs)

    assert flag is False
    assert result["status"] == 500
    assert b"Internal server error" in result["response"].data

