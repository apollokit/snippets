
import logging

import log as tlog
# *note* make sure to call this function once at your entry python script to
# configure logging
tlog.basicLoggingConfig()

from logging_import_example import do_stuff


# uncomment for log messages to use relative time instead of absolute time
# tlog.setLogTimeRelative()

# here we can manually control the verbosity of logging_import_example
# module (as desired)
# test_module_logger = logging.getLogger('logging_import_example')
# test_module_logger.setLevel(logging.DEBUG)

# This names the logger with the name of the current module
logger = tlog.getLogger(__name__)

# Set logger for both this file and the import to this level
tlog.setAllLoggerLevels('debug')


# make sure to use %s style string formatting instead of f-strings (f"blah")
# need to do this because f-strings will be rendered in a logger call even
# the log level for that specific call is being ignored
#  see https://stackoverflow.com/questions/54367975/python-3-7-logging-f-strings-vs
logger.critical("hey %d", 1)
logger.error("hey %d", 2)
logger.warning("hey %d", 3)
logger.important("hey %d", 4)
logger.info("hey %d", 5)
# might not print, depending on default level in log.py
logger.debug("hey %d", 6)

do_stuff()
