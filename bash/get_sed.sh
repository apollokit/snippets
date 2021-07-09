# Return the right sed executable to use based on OS platform
# use in makefiles:
#     sed=$(shell ./get_sed.sh)

if [[ $(uname) == "Linux" ]]; then
    echo sed
# use gsed on Mac (Darwin) because the built in sed works differently from standard linux sed
elif [[ $(uname) == "Darwin" ]]; then
    echo gsed
fi
