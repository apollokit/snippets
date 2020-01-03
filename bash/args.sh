parent_dir=$1
job_dir=$2

shift 2

if [ "$1" == "--ci_test" ]; then
    ci_test_arg="--ci_test"
fi