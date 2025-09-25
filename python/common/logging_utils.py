import logging
import uuid
from contextvars import ContextVar

from python.common.verbose_logging import VERBOSE_LEVEL_NUM, verbose

# Context variables for request-scoped data
request_id_var: ContextVar[str] = ContextVar('request_id', default='N/A')

class ContextLogger:
    """Logger that automatically includes context information"""
    
    def __init__(self, name):
        # logging.addLevelName(VERBOSE_LEVEL_NUM, 'VERBOSE')
        self.logger = logging.getLogger(name)
        self.logger.verbose = verbose
    
    def _get_extra(self, **kwargs):
        """Get extra fields with defaults"""
        return {
            'request_id': request_id_var.get(),
            **kwargs
        }
    
    def info(self, message, **kwargs):
        self.logger.info(message, extra=self._get_extra(**kwargs))
    
    def error(self, message, **kwargs):
        self.logger.error(message, exc_info=True, extra=self._get_extra(**kwargs))
    
    def warning(self, message, **kwargs):
        self.logger.warning(message, extra=self._get_extra(**kwargs))
    
    def debug(self, message, **kwargs):
        self.logger.debug(message, extra=self._get_extra(**kwargs))

    def verbose(self, message, **kwargs):
        self.logger.verbose(message, extra=self._get_extra(**kwargs))        

# Context managers for setting context
class RequestContext:
    """Context manager for request-scoped logging"""
    
    def __init__(self, request_id=None):
        self.request_id = request_id or str(uuid.uuid4())[:8]
        self.tokens = []
    
    def __enter__(self):
        self.tokens.append(request_id_var.set(self.request_id))
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        for token in reversed(self.tokens):
            token.var.reset(token)

# Usage examples
def get_logger(name):
    """Get a context-aware logger"""
    return ContextLogger(name)

# Example usage in Flask/Django middleware
def setup_request_context(request):
    """Set up logging context for a request"""
    request_id = getattr(request, 'request_id', str(uuid.uuid4())[:8])
    
    return RequestContext(
        request_id=request_id
    )