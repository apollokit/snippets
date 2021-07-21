# Note: sometimes you can might trouble getting to a debug command line, 
# usually (exclusively?) when python is being run within a subshell started by 
# another program. In such cases, worth trying this:
# export PYTHONUNBUFFERED=1
# see:
#   - https://emacs.stackexchange.com/questions/21948/cant-see-pdb-output-from-shell-mode
#   - https://stackoverflow.com/a/59812588/4292910

import ipdb
ipdb.set_trace()
