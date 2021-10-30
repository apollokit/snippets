
# remove files with regular expression
ls | grep -P "^A.*[0-9]{2}$" | xargs -d"\n" rm
