#!/bin/bash
set -ex

SCRIPT_DIR=$(dirname $(realpath $0))
python_version=3.7
# python_version=3.8

virtualenv_dir=~/.config/virtualenvs/pysnip

# If the virtualenv already exists, just update requirements.
if [ -e "$virtualenv_dir" ]; then
    echo "$virtualenv_dir already exists. We'll just update requirements."
else
    /usr/bin/python${python_version} -m venv "$virtualenv_dir"

    # pip also needs an upgrade, for some requirements (hardcoded version here for now)
    $virtualenv_dir/bin/pip install --upgrade pip
fi

# Now install requirements.
$virtualenv_dir/bin/pip install -r "$SCRIPT_DIR/requirements.txt"