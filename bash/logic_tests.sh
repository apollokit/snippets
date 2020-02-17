# https://stackoverflow.com/a/13864829
# check if var is not the empty string (will be an empty string if it doesn't
# exist)
if [ ! -z "$var" ]; then
    echo "exists"
else
    echo "doesnt exist"
fi

#  test if file /sys/module/hid_apple/parameters/fnmode only has "1" in it
if [ "$(cat /sys/module/hid_apple/parameters/fnmode)" == "1" ]; then
    echo 'hi'
fi