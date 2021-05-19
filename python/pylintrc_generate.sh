pylint --generate-rcfile > .pylintrc

# but make sure to include
#  [MASTER]
# init-hook='import sys; sys.path.append("./library")'
# if pylint needs to know where a library is