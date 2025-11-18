import logging


class CustomLogFormatter(logging.Formatter):
    """Custom formatter that handles optional extra fields gracefully"""
    
    def format(self, record):
        # Add default values for optional fields if they don't exist
        if not hasattr(record, 'request_id'):
            record.request_id = 'N/A'
        
        return super().format(record)