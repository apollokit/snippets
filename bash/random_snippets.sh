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



## count number of files in a dir
ls /net/datasets/raw_originals/201912190759_NvmhiQ/output/vb100/vb100_video/American_Rock_Wren  | wc -l

## count the number of files in all subdirs (where vb100_video contains only subdirs, no regular files)
let a=0
for dir in $(ls -d /net/datasets/raw_originals/201912190759_NvmhiQ/output/vb100/vb100_video/*)
do
    num_files=$(ls $dir | wc -l)
    let "a = $a + $num_files"
done
echo $a # the number of files accumulated across all subdirs


## split a string on a delimiter
# https://stackoverflow.com/a/14314206
echo "bla@some.com/john@home.com" | awk -F'/' '{print $1,$2}'
# output: bla@some.com john@home.com
echo "macos/Default (OSX).sublime-keymap" | awk -F '/' '{print $2}'
# output: Default (OSX).sublime-keymap


## Boolean var for if control flow
# from https://stackoverflow.com/a/2953673/4292910
the_world_is_flat=true
# ...do something interesting...
if [ "$the_world_is_flat" = true ] ; then
    echo 'Be careful not to fall off!'
fi
