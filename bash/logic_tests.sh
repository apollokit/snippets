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

# test file existence
# execute the custom mod launch file if it's available
if [ -e "$launch_dir/osr_mod.launch" ]; then
    bash -i -c "roslaunch osr_bringup osr_mod.launch"
# otherwise go with the default
else
    bash -i -c "roslaunch osr_bringup osr.launch"
fi

# only install if it doesn't exist
script_file=$(which markdown-enum)
if [ "$script_file" == "" ]; then
    pip install enumerate-markdown
fi

