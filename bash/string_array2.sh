declare -a buckets=( \
    "dynsim65-dynsim65-kit-20210530212757" \
    "dynsim65-dynsim65-kit-20210601110828" \
    "dynsim65-dynsim65-kit-20210601161437" \
    "dynsim65-dynsim65-kit-20210601222836" \
    "dynsim65-dynsim65-kit-20210602092413" \
    )

declare -a scenarios=( \
    "truth" \
    "baseline" \
    "scenario3" \
    "scenario4" \
    "scenario5" \
    )


# i is the index1
for i in "${!buckets[@]}"; do
    echo "${scenarios[$i]}"
    echo "   ${buckets[$i]}"
done