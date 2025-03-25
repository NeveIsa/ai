import networkx as nx

from search.algos import bfs, dfs

from viz.grid import animate
from fire import Fire


def main(n, algo):
    g = nx.grid_2d_graph(n, n)
    start = (round(n / 2), round(n / 2))
    if algo == "dfs":
        v = dfs(g, start)
    elif algo == "bfs":
        v = bfs(g, start)
    else:
        print(f"Unsupported algo {algo}")

    animate(g, v)


Fire(main)
