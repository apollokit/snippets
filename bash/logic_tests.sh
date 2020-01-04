# https://stackoverflow.com/a/13864829
# check if var is not the empty string (will be an empty string if it doesn't
# exist)
if [ ! -z "$var" ]; then
    echo "exists"
else
    echo "doesnt exist"
fi
