#!/bin/bash
set -e

# Start the ssh agent and store its environment in case it's needed later.
SSH_ENV=$HOME/.ssh/kitbox0-tmux-kit-environment
echo "Running ssh agent"
ssh-agent -s > $SSH_ENV
chmod 0600 $SSH_ENV
. $SSH_ENV
# Add my key
ssh-add ~/.ssh/id_rsa

# create new session and execute shell command immediately
# unfortunately, I don't think there's an easy way to put 
# ...the shell command on a separate line
tmux new-session -d -s "dictate" 'cd /home/kit/git/better_dictate && ./run.sh'

# make a new pane and execute command
tmux split-window -v 'cd /home/kit/git/better_dictate/frontend && ./run.sh'

# Base window
tmux rename-window base

# could also do...
# tmux new-window -n ipython #'source ~/vinci/stockbot/source_virtualenv && ipython'

# not necessary
# tmux select-window -t 0

# attach
tmux a