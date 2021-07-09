import log as sflog

# note: use module name
logger = sflog.getLogger(__name__)
# can also set to a desired name, but this is discouraged
# logger = sflog.getLogger('foo')

def do_stuff():
    logger.info('stuff is done')
    logger.debug('I said, stuff is done!')
