python3.8 -c "import sys; print(sys.path)"
python3.8 -Sc "import sys; print(sys.path)"

# site
python -m site
python -c 'import site; print(site.getsitepackages())'
python -m site --user-site