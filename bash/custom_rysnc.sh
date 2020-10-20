function myrsync() {
    function usage() {
        echo "usage: vrsync <remote host> <-v>"
        echo "    remote host is the host, like '192.168.1.29' or 'myrpi4'"
        echo "    -v for verbose"
        return 0
    }
    remote_host=$1
    [ "$remote_host" == "" ] && usage && return 1
    verbose_opt=$2
    shift 2

    # the directory on the local machine (e.g. your dev desktop)
    local_source_dir="/home/kit/foo"
    # the directory on the remote machine (e.g. the rpi)
    remote_destination_dir="/home/ubuntu/temp"

    pushd $local_source_dir
    # rsync: updates changed (including new) files from a source to a destination. 
    # Note: this code will not overwrite source files with files files from destination, but it's always best to be careful!
    # rsync's everything in the local_source_dir to remote_destination_dir, excluding ".git" (for when it's a git repo)
    echo "rsync -a --update --exclude '.git/*' $verbose_opt . ubuntu@$remote_host:$remote_destination_dir"
    rsync -a --update --exclude '.git/*' $verbose_opt . ubuntu@$remote_host:$remote_destination_dir
    popd
}
# you can call this alias from the command line, directly
alias myrsyncrpi="myrsync 192.168.1.29"
# ...or the verbose version
alias myrsyncrpiv="myrsync 192.168.1.29"