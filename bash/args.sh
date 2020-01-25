function usage {
    # arg_one is required, arg two is optional
    echo "$0 arg_one <arg_two>"
    exit 1
}

arg_one=$1
arg_two=$2

# this one's required
[ "$arg_one" == "" ] && usage
# default is foo
[ "$arg_two" == "" ] && arg_two="foo"
# make sure it's either "foo" or "bar"
( ! ( [ "$arg_two" == "foo" ] || [ "$arg_two" == "bar" ] ) ) && echo "arg_two must be 'foo' or 'bar'"


shift 2

if [ "$1" == "--ci_test" ]; then
    ci_test_arg="--ci_test"
fi
