# get cuda version using cut
# -d " " marks space as the delimiter
# -f15 means choose the 15th element that was cut
cuda_ver=$(nvidia-smi | grep "CUDA Version" | cut -d " " -f15)