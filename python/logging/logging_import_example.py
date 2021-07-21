import log as tlog

# note: use module name
logger = tlog.getLogger(__name__)
# can also set to a desired name, but this is discouraged
# logger = tlog.getLogger('foo')

def do_stuff():
    logger.info('stuff is done')
    logger.debug('I said, stuff is done!')
