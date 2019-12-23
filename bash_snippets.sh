## echo every file name (no white spaces in file names!)
files=$(ls snippets/python/*)
for value in $files
do
    echo $value
done


## copy a bunch of file name to dest_dir
# note the use of double quotes in the cp line, that's to escape spaces
# this works under macos, couldn't get xargs to work with cp because there's no -t option
files1=snippets/python/*
files2=macos/* 
files3=settings/* 
for value in $files1
do
    # echo "$value"
    cp "$value" "$dest_dir"
done
for value in $files2
do
    # echo "$value"
    cp "$value" "$dest_dir"
done
for value in $files3
do
    # echo "$value"
    cp "$value" "$dest_dir"
done


## cp a bunch of files, listed as different lines in a text file blah.txt
cat ../temp/blah.txt | xargs cp -r -t <destination>


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