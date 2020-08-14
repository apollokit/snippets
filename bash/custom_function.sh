# example of a custom command line func with a usage prompt when no arg is provided
custom_function() {
    function usage() {
        echo "usage: $ custome_function <file>"
        return 0
    }
    [ "$1" = "" ] && usage && return 1
    cat "$1" | tr -d " \t\n\r"
}