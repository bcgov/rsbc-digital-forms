from flask import jsonify, Response, send_file
from minio import Minio
from minio.error import S3Error
from io import BytesIO
import os
import mimetypes
from datetime import timedelta
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config

logger = get_logger(__name__)
INTERNAL_SERVER_ERROR="Internal server error"

minio_client = Minio(
    Config.MINIO_BUCKET_URL,
    access_key=Config.MINIO_AK,
    secret_key=Config.MINIO_SK,
    secure=getattr(Config, 'MINIO_SECURE', False)
)
BUCKET = getattr(Config, 'MINIO_BUCKET', 'rsbc-static-files')

def upload_file(**kwargs):
    """Uploads a file to MinIO"""
    request = kwargs.get('request')
    file = request.files.get('file') if request else None
    object_name = request.form.get('object_name') if request else None
    if not object_name and file:
        object_name = file.filename

    if not file:
        kwargs['response'] = jsonify({"error": "No file uploaded"})
        kwargs['status'] = 400
        return False, kwargs
    
    try:
        data = file.read()
        stream = BytesIO(data)
        minio_client.put_object(BUCKET, object_name, stream, length=len(data))

        # Build success response in kwargs
        kwargs['response'] = jsonify({"message": f"{object_name} uploaded successfully"})
        kwargs['status'] = 201
        return True, kwargs
    except S3Error as e:
        logger.error(f"Error uploading file: {e}")
        kwargs['response'] = jsonify({"error": "Failed to upload file"})
        kwargs['status'] = 500
        return False, kwargs
    
    except Exception as e:
        logger.error(f"Unexpected error while generating presigned URL: {e}")
        kwargs['response'] = jsonify({"error": INTERNAL_SERVER_ERROR})
        kwargs['status'] = 500
        return False, kwargs



def get_file_stream(**kwargs):
    """Streams a file to the caller"""
    filename = kwargs.get('filename')
    mimetype, _ = mimetypes.guess_type(filename)

    if mimetype is None:
        # fallback if unknown
        mimetype = "application/octet-stream"

    try:
        obj = minio_client.get_object(BUCKET, filename)

        # Define generator for streaming
        def generate():
            for chunk in obj.stream(32 * 1024):
                yield chunk
            obj.close()
            obj.release_conn()

        response = Response(
            generate(),
            mimetype=mimetype,
            headers={
                "Content-Disposition": f'inline; filename="{os.path.basename(filename)}"'
            },
        )

        kwargs["response"] = response
        kwargs["status"] = 200
        return True, kwargs
    except S3Error as e:
        logger.warning(f"File not found: {e}")
        kwargs['response'] = jsonify({"error": "Not found"})
        kwargs['status'] = 404
        return False, kwargs
    except Exception as e:
        logger.error(f"Unexpected error while streaming file '{filename}': {e}")
        kwargs['response'] = jsonify({"error": INTERNAL_SERVER_ERROR})
        kwargs['status'] = 500
        return False, kwargs


def generate_presigned_url(filename, expiry=3600, **kwargs):
    """Generates a presigned URL for downloading or viewing a file"""
    try:
        # Check if the object exists
        minio_client.stat_object(BUCKET, filename)
    except S3Error as e:
        logger.warning(f"Cannot generate presigned URL, file not found: {filename}")
        kwargs['response'] = jsonify({"error": "File not found"})
        kwargs['status'] = 404
        return False, kwargs
    
    try:
        # Convert seconds to timedelta
        expires = timedelta(seconds=expiry)
        url = minio_client.presigned_get_object(BUCKET, filename, expires=expires)

        kwargs['response'] = jsonify({
            "filename": filename,
            "url": url,
            "expiry": expiry
        })
        kwargs['status'] = 200
        return True, kwargs

    except S3Error as e:
        logger.error(f"Error generating presigned URL for '{filename}': {e}")
        kwargs['response'] = jsonify({"error": "Unable to generate presigned URL"})
        kwargs['status'] = 500
        return False, kwargs

    except Exception as e:
        logger.error(f"Unexpected error while generating presigned URL: {e}")
        kwargs['response'] = jsonify({"error": INTERNAL_SERVER_ERROR})
        kwargs['status'] = 500
        return False, kwargs



def list_files(**kwargs):
    """Lists objects in the bucket"""
    prefix = kwargs.get('prefix')
    try:
        objects = minio_client.list_objects(BUCKET, prefix=prefix, recursive=True)
        items = [{
            "object_name": obj.object_name,
            "size": obj.size,
            "last_modified": obj.last_modified.isoformat() if obj.last_modified else None
        } for obj in objects]

        kwargs['response'] = jsonify({"items": items})
        kwargs['status'] = 200
        return True, kwargs
    except S3Error as e:
        # Use warning/error instead of exception for your custom ContextLogger
        logger.error(f"Error listing files from bucket '{BUCKET}': {e}")
        kwargs['response'] = jsonify({"error": "Unable to list files"})
        kwargs['status'] = 500
        return False, kwargs
    except Exception as e:
        logger.error(f"Unexpected error while listing files: {e}")
        kwargs['response'] = jsonify({"error": INTERNAL_SERVER_ERROR})
        kwargs['status'] = 500
        return False, kwargs


def delete_file(**kwargs):
    """Deletes an object"""
    filename = kwargs.get('filename')
    if not filename:
        kwargs['response'] = jsonify({"error": "Filename not provided"})
        kwargs['status'] = 400
        return False, kwargs
    try:
         # Check if the file exists. If not minio will throw an exception.
        minio_client.stat_object(BUCKET, filename)

        minio_client.remove_object(BUCKET, filename)
        kwargs['response'] = jsonify({"message": f"{filename} deleted successfully"})
        kwargs['status'] = 200
        return True, kwargs
    except S3Error as e:
       # Handle missing file or other MinIO errors
        if e.code == "NoSuchKey":
            logger.warning(f"File not found: {filename}")
            kwargs['response'] = jsonify({"error": f"File '{filename}' not found"})
            kwargs['status'] = 404
        else:
            logger.error(f"S3 error while deleting '{filename}': {e}")
            kwargs['response'] = jsonify({"error": "S3 operation failed"})
            kwargs['status'] = 500
        return False, kwargs
    except Exception as e:
        # Handle unexpected issues
        logger.error(f"Unexpected error deleting '{filename}': {e}")
        kwargs['response'] = jsonify({"error": INTERNAL_SERVER_ERROR})
        kwargs['status'] = 500
        return False, kwargs
