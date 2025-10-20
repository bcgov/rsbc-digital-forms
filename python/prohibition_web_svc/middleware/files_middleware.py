from flask import jsonify, Response, send_file
from minio import Minio
from minio.error import S3Error
from io import BytesIO
import os
from datetime import timedelta
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config

logger = get_logger(__name__)

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
    file = request.files.get('file')
    object_name = request.form.get('object_name') or (file.filename if file else None)
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    try:
        data = file.read()
        stream = BytesIO(data)
        minio_client.put_object(BUCKET, object_name, stream, length=len(data))

       # Build a proper response here
          # Return flag + args mapping
        kwargs['response'] = jsonify({"message": f"{object_name} uploaded successfully"})
        kwargs['status'] = 201
        return True, kwargs
    except S3Error as e:
        logger.exception("Error uploading file: %s", e)
        response = jsonify({"error": "Failed to upload file"})
        return False, {"response": jsonify({"error": "Failed to upload file"}), "status": 500}


def get_file_stream(filename):
    """Streams a file to the caller"""
    try:
        obj = minio_client.get_object(BUCKET, filename)
        def generate():
            for chunk in obj.stream(32 * 1024):
                yield chunk
            obj.close()
            obj.release_conn()
        return Response(generate(), mimetype="application/octet-stream",
                        headers={'Content-Disposition': f'attachment; filename=\"{os.path.basename(filename)}\"'})
    except S3Error as e:
        logger.warning("File not found: %s", e)
        return jsonify({"error": "Not found"}), 404


def generate_presigned_url(filename, expiry_seconds):
    """Generate a temporary URL for the file"""
    try:
        url = minio_client.presigned_get_object(BUCKET, filename, expires=timedelta(seconds=expiry_seconds))
        return jsonify({"url": url})
    except S3Error as e:
        logger.exception("Error generating presigned URL: %s", e)
        return jsonify({"error": "Failed to generate URL"}), 500


def list_files(prefix):
    """Lists objects in the bucket"""
    try:
        objects = minio_client.list_objects(BUCKET, prefix=prefix, recursive=True)
        items = [{
            "object_name": obj.object_name,
            "size": obj.size,
            "last_modified": obj.last_modified.isoformat() if obj.last_modified else None
        } for obj in objects]
        return jsonify({"items": items})
    except S3Error as e:
        logger.exception("Error listing files: %s", e)
        return jsonify({"error": "Unable to list files"}), 500


def delete_file(filename):
    """Deletes an object"""
    try:
        minio_client.remove_object(BUCKET, filename)
        return jsonify({"message": f"{filename} deleted successfully"})
    except S3Error as e:
        logger.exception("Error deleting file: %s", e)
        return jsonify({"error": "Unable to delete file"}), 500
