#!/bin/bash

set -e

build_id=12345

echo "Check if cloud build id $build_id is finished"

# timeout to wait for build
timeout_mins=20 
timeout_s=$(($timeout_mins*60))

SECONDS=0
# gives time since setting SECONDS to 0
duration=$SECONDS
while (($duration < $timeout_s)); do
    success_lines=$(gcloud builds describe $build_id | grep "status: SUCCESS" | wc -l)
    # do we see "status: SUCCESS" in output at least once?
	if (($success_lines > 0)); then
		echo "Cloud build finished!"
		# exit 0, success
        exit 0
	fi
	
    duration=$SECONDS
    # wait 30 seconds, seems a good amount of time to not poll too often
	sleep 30
done

echo "Cloud build timed out, quitting"
# non-zero exit, fail
exit 1