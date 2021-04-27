pip install snakeviz

python -m cProfile -o results.prof foo.py

snakeviz results.prof

echo "open http://127.0.0.1:8080"