#!/bin/bash

# see https://unix.stackexchange.com/a/278942
datetime=$(date +"%FT%H%M%S")

# make a file with name like status_2020-09-15T215450.txt
touch status_$datetime.txt