"""[summary]

Usage: 
    python logging_example.py -v debug go
"""

import logging

import click

import log as sflog
sflog.basicLoggingConfig()

from logging_import_example import do_stuff


# uncomment for log messages to use relative time instead of absolute time
# sflog.setLogTimeRelative()

# This names the logger with the name of the current module
logger = sflog.getLogger(__name__)

# here we can manually control the verbosity of logging_import_example
# module (as desired)
# test_module_logger = logging.getLogger('logging_import_example')
# test_module_logger.setLevel(logging.DEBUG)

# uncomment if a log message prefix is desired
# sflog.set_log_prefix('Blah: ')

@click.group()
@sflog.simpleVerbosityOption()
def cli():
    """This function is necessary for the click CLI to work."""


@cli.command()
def go():
    # make sure to use %s style string formatting instead of f-strings (f"blah")
    # need to do this because f-strings will be rendered in a logger call even
    # the log level for that specific call is being ignored
    #  see https://stackoverflow.com/questions/54367975/python-3-7-logging-f-strings-vs
    logger.critical("hey %d", 1)
    logger.error("hey %d", 2)
    logger.warning("hey %d", 3)
    logger.important("hey %d", 4)
    logger.info("hey %d", 5)
    logger.debug("hey %d", 6)

    do_stuff()

if __name__ == '__main__':
    cli()
