# https://stackoverflow.com/a/691157
declare -A newmap
newmap[name]="Irfan Zulfiqar"
newmap[designation]=SSE
newmap[company]="My Own Company"

echo ${newmap[company]}
echo ${newmap[name]}