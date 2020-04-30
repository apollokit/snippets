# Hints

- Dealing with "Attempted relative import in non-package" error
    - from a line like "from .fusion360_lib import utils"
    - usually this is because you're trying to run a script as __main__, when it's embedded within a package. You can't really do this cleanly, and you need to modify your sys.path to get it to work
    - but if you use that relative import in a python file that's not run as __main__ (it's imported and run in another .py file) then it'll work