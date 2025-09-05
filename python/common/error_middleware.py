# Error middleware functions
import json
import traceback
import logging
import functools
import inspect
from flask import request, current_app
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

from python.common.enums import EventType, ErrorCode, ErrorSeverity, ErrorStatus, ErrorCategory
from python.common.models.base import db
from python.common.models.df_errors import DFErrors
from python.common.models.event import Event

def get_safe_payload():
    """
    Safely extract and serialize the request payload.
    """
    try:
        # Try to get JSON payload
        payload = request.get_json(silent=True)
        if payload is not None:
            return json.dumps(payload)
        
        # If not JSON, try to get form data
        payload = request.form.to_dict()
        if payload:
            return json.dumps(payload)
        
        # If no form data, get query parameters
        payload = request.args.to_dict()
        if payload:
            return json.dumps(payload)
        
        # If all else fails, return a message indicating no payload
        return json.dumps({"message": "No payload found in request"})
    except Exception as e:
        return json.dumps({"message": "No payload found in request"})

def get_function_info(func):
    """
    Extract detailed information about the function or method.
    """
    module = inspect.getmodule(func)
    if module:
        module_name = module.__name__
    else:
        module_name = "unknown_module"
    
    if inspect.ismethod(func):
        class_name = func.__self__.__class__.__name__
        return f"{module_name}.{class_name}.{func.__name__}"
    elif inspect.isfunction(func):
        return f"{module_name}.{func.__name__}"
    else:
        return f"{module_name}.unknown_function"

def record_error(error_code: ErrorCode, error_details, event_id: int = None, submission_id: int = None, event_type: EventType = None, ticket_no=None, func=None, payload=None):
    """
    Record an error in the database.
    """
    try:
        
        function_path = get_function_info(func) if func else "unknown"
        
        if not payload:
            payload = get_safe_payload()
            
        # Handle stack trace extraction if error_details is an exception
        if isinstance(error_details, Exception):
            stack_trace = ''.join(traceback.format_exception(type(error_details), error_details, error_details.__traceback__))
        else:
            stack_trace = str(error_details)

        error_log = DFErrors(
            error_cd=str(error_code.code),
            error_cd_desc=str(error_code.description),
            error_category_cd=str(error_code.category),
            error_resolution=str(error_code.resolution),
            error_severity_level_cd=str(error_code.severity),
            error_status_cd=str(ErrorStatus.NEW),
            event_id=event_id,
            submission_id=submission_id,
            event_type=str(event_type) if event_type else None,
            ticket_no=ticket_no,
            req_payload=payload,
            error_details=stack_trace,
            error_path=function_path,
            created_by='SYSTEM',
            received_dt=datetime.now(),
        )
        db.session.add(error_log)
        db.session.commit()
        logging.error(f"Error recorded: {error_code} - {error_code.description} - Event ID: {event_id} - Event Type: {event_type} - Function: {function_path} - {error_details}")
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Failed to record error: {error_code} - {error_code.description} - Event ID: {event_id} - Event Type: {event_type} - Function: {function_path} - {error_details}")

def error_handler(func):
    """
    Decorator to handle errors in functions.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_code = ErrorCode.G00  # Default to general error
            error_details = str(e)
            
            # Attempt to get event_id from kwargs or request
            event_id = kwargs.get('event_id')
            if not event_id and hasattr(request, 'view_args'):
                event_id = request.view_args.get('event_id')
            
            if not event_id:
                current_app.logger.warning("No event_id found for error logging")
                event_id = None  # or some default value
            
            record_error(error_code, error_details, event_id, func=func)
            raise  # Re-raise the exception after recording
    return wrapper