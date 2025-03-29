from games import maze
from search.algos import bfs, dfs
import plotext as plt
from time import sleep
from fire import Fire

G = maze.Graph(maze.grid)

# print(G.neighbors((4, 2)))


def goalfn(node):
    if node == (0, 7):
        return True
    else:
        return False


def main(algo):
    if algo == "bfs":
        algo = bfs
    elif algo == "dfs":
        algo = dfs

    out = algo(G, start=(4, 2), goalfn=goalfn)
    grid = maze.grid

    for i in range(len(out)):
        for o in out[: i + 1]:
            grid[o[0], o[1]] = 100
        # print(grid.T)
        plt.matrix_plot(grid.T.tolist())
        plt.show()
        sleep(0.2)


Fire(main)
