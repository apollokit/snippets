declare -a videos=( \
    "s3://fancycam-videos/vb100/Acorn_Woodpecker_00001.mp4" \
    "s3://fancycam-videos/vb100/Acorn_Woodpecker_00002.mp4" \
    "s3://fancycam-videos/vb100/Acorn_Woodpecker_00003.mp4" \
    "s3://fancycam-videos/vb100/Acorn_Woodpecker_00004.mp4" \
    "s3://fancycam-videos/vb100/Acorn_Woodpecker_00005.mp4" \
    "s3://fancycam-videos/vb100/Acorn_Woodpecker_00006.mp4" \
    "s3://fancycam-videos/vb100/Acorn_Woodpecker_00007.mp4" \
    )


for video in "${videos[@]}"
do
    echo "./env.sh python dataset-vb100-create.py go \
        --corpus_parent_dir $CORPUS_PARENT_DIR \
        --video_url $video"
    ./env.sh python dataset-vb100-create.py go \
        --video_url $video
done