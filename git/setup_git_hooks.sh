repo_base=../../..
hooks_dir=$repo_base/.git/hooks

pushd $hooks_dir

ln -s <path from repo base>/pre-commit pre-commit

popd