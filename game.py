from games import gridgame as gg
from search.algos import bfs, dfs
import plotext as plt
import numpy as np

G = gg.Graph(gg.grid)

# print(G.neighbors((4, 2)))


def goalfn(node):
    print(node)
    if node == (0, 7):
        return True
    else:
        return False


out = bfs(G, start=(4, 2), goalfn=goalfn)

grid = gg.grid

for i in range(len(out)):
    for o in out[:i]:
        grid[o[0], o[1]] = 200
    print(grid.T)
    plt.heatmap(np.eye(3))
    input()
