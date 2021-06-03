# check distro
uname_out=$(uname -a)
if [[ $uname_out == *"Linux"* ]]; then
    echo "Linux"
elif [[ $uname_out == *"Darwin"* ]]; then
    echo "Darwin (macos)"
else
    echo "other, uname:"
    echo "$uname_out"
fi