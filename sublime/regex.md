# Using match groups

## Task

Replace all patterns that look like
"
x

pad byte
"

with 
"x  pad byte"

## How

Search and replace

find: "(.)\n\n(.)"
replace: "$1 $2"

See image in this dir