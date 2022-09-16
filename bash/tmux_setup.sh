#!/bin/bash
set -e

# Start the ssh agent and store its environment in case it's needed later.
# SSH_ENV=$HOME/.ssh/kitbox0-tmux-kit-environment
# echo "Running ssh agent"
# ssh-agent -s > $SSH_ENV
# chmod 0600 $SSH_ENV
# . $SSH_ENV
# # Add my key
# ssh-add ~/.ssh/id_rsa

# create new session, rename initial window to "base"
tmux new-session -d -s "dictate"
tmux rename-window base

# run backend in first pane (got the send command from https://serverfault.com/a/339451)
tmux send -t dictate:base.0 'cd ~/git/better_dictate && ./run.sh' ENTER

# run frontend in separate pane
tmux split-window -v 
tmux send -t dictate:base.1 'cd ~/git/better_dictate/frontend && ./run.sh' ENTER

# not necessary
# tmux select-window -t 0

# attach
tmux a -t dictate