# works on Mac

# Don't run this file!


######  Linux

# replace in place without a backup
sed -i  "s/yo/and/" blah.txt


######  MacOS
# (it's incompatible with linux :( )

# for a file blah.txt with line "DOTFILES_DIR=<autopopulate in setup.sh>", will replace the "<autopopulate in setup.sh>" with the path to dotfiles_dir. Note the use of | as an alternative delimiter to /, because the /'s in the file path would f it up.
# makes a backup of original file in ..._orig
sed -i"_orig" "s|DOTFILES_DIR=<autopopulate in setup.sh>|DOTFILES_DIR=$(get_abs_path $dotfiles_dir)|" blah.txt

# replace in place without a backup
sed -i""  "s/yo/and/" blah.txt