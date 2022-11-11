#!/bin/bash

# see https://unix.stackexchange.com/a/278942
datetime=$(date +"%FT%H%M%S")

# bash timestamp filename
# outputs 2022_10_21_19_15_11
$(date -u +'%Y_%m_%d_%H_%M_%S')
$(date -u +'%Y%m%d%H%M%S')

# make a file with name like status_2020-09-15T215450.txt
touch status_$datetime.txt