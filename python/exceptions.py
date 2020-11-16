import sys, traceback

try:
    1 / 0
except Exception as e: # (as opposed to except Exception, e:)
                       # ^ that will just look for two classes, Exception and e
    # for the repr
    print(repr(e))
    # for just the message, or str(e), since print calls str under the hood
    print(e)
    # the arguments that the exception has been called with. 
    # the first one is usually the message. (OSError is different, though)
    print(e.args)

    # see https://docs.python.org/3/library/traceback.html
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback)
