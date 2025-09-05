import logging;

VERBOSE_LEVEL_NUM: int = 5

def verbose(message, *args, **kwargs):
    logging.log(VERBOSE_LEVEL_NUM, message, *args, **kwargs)