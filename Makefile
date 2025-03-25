default:
	python test.py --n=50 --algo=bfs
	python test.py --n=50 --algo=dfs

deps:
	uv pip install -r req.txt || pip install -r req.txt

