"""

Original code courtesy of Mike Dussault from VinciLab.

Some of this code is tightly coupled with the click CLI library. 
That code is all called out at the bottom of this file

Required reading: https://pymotw.com/3/logging/index.html
"""

from datetime import datetime
from functools import partial
import logging
from typing import Dict

import click
import click_log

## Defaults

DEFAULT_LOG_LEVEL = 'INFO'

DEFAULT_ABS_LOG_FORMAT = "%(asctime)s %(levelname)-10s %(module)-25s %(message)s"
DEFAULT_REL_LOG_FORMAT = "%(relativeCreatedPretty)s %(levelname)-10s %(module)-25s %(message)s"

DEFAULT_ABS_LOG_TIME_FORMAT = "%H:%M:%S"
DEFAULT_REL_LOG_TIME_FORMAT = "r%H:%M:%S"
# with fractional seconds
# DEFAULT_REL_LOG_TIME_FORMAT = "r%H:%M:%S.%f"

DEFAULT_LOG_FORMAT = DEFAULT_ABS_LOG_FORMAT
DEFAULT_LOG_TIME_FORMAT = DEFAULT_ABS_LOG_TIME_FORMAT

# All messages will be prefixed with this. See set_prefix(). This is useful for 
# tagging all of a worker's log messages with a prefix so each worker can be 
# distinguished from the others.
_log_prefix = ''

# default global log level
_log_level = DEFAULT_LOG_LEVEL

# _log_format = DEFAULT_LOG_FORMAT
_log_time_format = DEFAULT_LOG_TIME_FORMAT

# a registry to keep track of the loggers that have been created
# todo: how does this work with multi-processing?
_logger_registry: Dict[str, logging.Logger] = {}

# custom log levels
# more important than info
IMPORTANT = logging.INFO + 1
logging.addLevelName(IMPORTANT, "IMPORTANT")
# super low important, used for getting a better understanding of control flow 
# in the code
CODETRACE = logging.DEBUG - 1
logging.addLevelName(CODETRACE, "CODETRACE")

# all the log levels
# must include custom levels as well
# custom levels need bespoke handling in getLogger()
LOG_LEVELS = ['CRITICAL', 'ERROR', 'WARNING', 'IMPORTANT', 'INFO', 'DEBUG', 'CODETRACE']

CUSTOM_FORMATTERS = {
    'CRITICAL': dict(fg='red', bold=True),
    'ERROR': dict(fg='red', bold=True),
    'WARNING': dict(fg='yellow'),
    'IMPORTANT': dict(fg='magenta'),
    'INFO': dict(fg='cyan'),
    'DEBUG': dict(fg='blue'),
    'CODETRACE': dict(fg='green')
}

## Custom formatting functionality


class CustomFormatter(logging.Formatter):
    """click_log's default formatter prints stuff like "warning: " in front of 
    warning and error messages. Better to just set the color of the whole line.
    """

    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt, datefmt)

    def format(self, record):
        if not record.exc_info:
            duration = datetime.utcfromtimestamp(
                record.relativeCreated / 1000)
            record.relativeCreatedPretty = duration.strftime(_log_time_format)

            # get the msg as formatted by logging.Formatter
            # e.g. 18:20:33 CRITICAL __main__        hey
            msg = super().format(record)

            msg = _log_prefix + msg

            level = record.levelname

            # add click color formatting to whole message
            if level in CUSTOM_FORMATTERS:
                msg = click.style(msg, **CUSTOM_FORMATTERS[level])
            else:
                levelno = record.levelno
                if levelno in CUSTOM_FORMATTERS:
                    msg = click.style(msg, **CUSTOM_FORMATTERS[levelno])

            return msg

        return logging.Formatter.format(self, record)


the_formatter = CustomFormatter(
    fmt=DEFAULT_LOG_FORMAT,
    datefmt=DEFAULT_LOG_TIME_FORMAT
)
click_log.core._default_handler.formatter = the_formatter


## Core api functions

def basicLoggingConfig():
    """This should be called from any top-level CLI files to setup logging
     for everything.

    *Note* need to call this, otherwise logging won't work

    This is the function that configures logging formatting for all of our 
    loggers
    """
    logger = logging.getLogger()

    click_log.basic_config(logger)

def setDefaultGlobalLevel(level: str = DEFAULT_LOG_LEVEL):
    """Set the default global log level for loggers created with 
    getLogger()

    *Note* must call this function before importing any other modules,
    because the default log level for individual modules is set at import-time.
    I.e., a module will only query this global level when it is first imported
    and its logger object is created

    Args:
        level: the logging level
    """
    assert level.upper() in LOG_LEVELS
    
    global _log_level # pylint: disable=global-statement
    _log_level = level.upper()

def setLogTimeAbsolute():
    """Set log messages to use absolute wall clock time
    """
    global _log_time_format
    the_formatter._style._fmt = DEFAULT_ABS_LOG_FORMAT
    the_formatter.datefmt = DEFAULT_ABS_LOG_TIME_FORMAT
    _log_time_format = DEFAULT_ABS_LOG_TIME_FORMAT

def setLogTimeRelative():
    """Set log messages to use time relative to start
    """
    global _log_time_format
    the_formatter._style._fmt = DEFAULT_REL_LOG_FORMAT
    the_formatter.datefmt = DEFAULT_REL_LOG_TIME_FORMAT
    _log_time_format = DEFAULT_REL_LOG_TIME_FORMAT

def getLogger(logger_name: str) -> logging.Logger:
    """Get a logger object to be used for logging in a module

    All project modules (python files) should use this function to create 
    a logger, before any other code in the module

    Args:
        logger_name: the name to use for the logger, normally it is
            the name of the module itself (i.e. __name__)

    Returns:
        a logger object to be used for logging
    """
    global _log_level # pylint: disable=global-statement
    logger = logging.getLogger(logger_name)
    logger.setLevel(_log_level)

    # add to the registry
    _logger_registry[logger_name] = logger

    # use a partial here so hat the log function is actually executed inline 
    # where important() is called. This preserves module naming in log output
    logger.important = partial(logger.log, IMPORTANT)
    logger.codeTrace = partial(logger.log, CODETRACE)

    return logger


def setAllLoggerLevels(level: str = 'INFO'):
    """Set the logging level for all registered loggers

    Set the logging level four all loggers created THUS FAR with
    getLogger()

    Note: not talking about the PNW logging industry here

    Args:
        level: the log level
    """
    assert level.upper() in LOG_LEVELS
    for logger in _logger_registry.values():
        logger.setLevel(level.upper())
    # need this so that subsequent module imports will default to the desired 
    # level
    setDefaultGlobalLevel(level)

def setLogPrefix(prefix: str):
    """Add a prefix to all logging output.

    Args:
        prefix: The prefix to add.
    """
    global _log_prefix  # pylint: disable=global-statement
    _log_prefix = prefix


class Decimator:
    """Basic decimation, useful for log messages

    This allows actions to be performed at a configurable rate. You query this
    object to determine if the next action should happen or not

    Usage:
        if sflog.decimator.decimate('blah.py 0', keep_every=120):
            logger.info("Hello world!")
    """

    def __init__(self):
        # counts log messages for each id
        self._log_counter: Dict[str, int] = {}

    def decimate(self, ID: str = 'aaa', keep_every: int = 1) -> bool:
        """Decimate an action with a given ID

        Will always return true on the first call for a given ID

        Args:
            ID: the id for the action, chosen by the user
            keep_every: determines how often actions should be dropped. 1 means
                keep every action, 2 means keep every second action, 3 every 
                third, etc

        Returns:
            True if action should take place, false if it should be skipped
        """
        self._log_counter.setdefault(ID, 0)
        counter = self._log_counter[ID]
        keep = (counter % keep_every) == 0
        self._log_counter[ID] += 1
        return keep

# default decimator
decimator = Decimator()

## Click related stuff

def simpleVerbosityOption(*names, **kwargs):
    '''A decorator that adds a `--verbosity, -v` option to the decorated
    click command.
    
    Name can be configured through ``*names``. Keyword arguments are passed to
    the underlying ``click.option`` decorator.
    '''

    if not names:
        names = ['--verbosity', '-v']

    kwargs.setdefault('default', _log_level)
    kwargs.setdefault('metavar', 'LVL')
    kwargs.setdefault('expose_value', False)
    kwargs.setdefault('help', 'Either ')
    kwargs.setdefault('is_eager', True)
    
    def decorator(f):
        def _set_level(ctx, param, value):
            if not value.upper() in LOG_LEVELS:
                raise click.BadParameter(
                    f'Must be one of {LOG_LEVELS}, not "{value}"')
            setAllLoggerLevels(value)

        return click.option(*names, callback=_set_level, **kwargs)(f)

    return decorator
