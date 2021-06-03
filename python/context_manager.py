# use for with statements
# 
# output:
# $ py context_manager.py 
# yo
# I'm here
# bye


import contextlib

@contextlib.contextmanager
def salutations():
    print("yo")

    try:
        yield
    finally:
        print("bye")

with salutations():
    print("I'm here")