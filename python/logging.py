# see here for logging formatters:
# https://docs.python.org/2/library/logging.html#logrecord-attributes
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

form = "%(asctime)s %(levelname)-8s %(funcName)-15s %(message)s"
logging.basicConfig(format=form,
                    datefmt="%H:%M:%S")

logger.debug("KeystrokeExec: typing keys")
