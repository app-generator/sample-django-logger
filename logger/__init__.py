import logging, sys
from logging import config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': 'DeployPRO,%(levelname)s %(message)s'
            },
        },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
            },
        'sys-logger6': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'facility': "local6",
            'formatter': 'verbose',
            },
        },
    'loggers': {
        'my-logger': {
            'handlers': ['sys-logger6','stdout'],
            'level': logging.DEBUG,
            'propagate': True,
            },
        }
    }

config.dictConfig(LOGGING) 

def logger(aText, aLevel=logging.DEBUG):

    LOGGER_instance = logging.getLogger("my-logger")

    if logging.DEBUG == aLevel:
        LOGGER_instance.debug(aText)
    elif logging.WARN == aLevel:    
        LOGGER_instance.warn(aText)
    elif logging.ERROR == aLevel:    
        LOGGER_instance.error(aText)
    elif logging.CRITICAL == aLevel:    
        LOGGER_instance.critical(aText)
    else: 
        LOGGER_instance.info(aText)

def logger_info(aText):
    logger(aText, aLevel=logging.INFO)

def logger_warn(aText):
    logger(aText, aLevel=logging.WARN)

def logger_err(aText):
    logger(aText, aLevel=logging.ERROR)

def logger_error(aText):
    logger(aText, aLevel=logging.ERROR)

def logger_critical(aText):
    logger(aText, aLevel=logging.CRITICAL)
