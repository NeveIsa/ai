import numpy as np
import plotext as plt

grid = np.zeros((8, 8))

START = 1
STOP = 100
OBSTACLE = 50

start = [5, 3]
stop = [1, 8]

obstacles = [
    (1, 7),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    (4, 7),
    (4, 8),
    (5, 5),
    (6, 5),
    (6, 6),
]

grid[start[0] - 1, start[1] - 1] = START
grid[stop[0] - 1, stop[1] - 1] = STOP
for obs in obstacles:
    grid[obs[0] - 1, obs[1] - 1] = OBSTACLE

grid = grid

# plt.matrix_plot(grid)


class Graph:
    def __init__(self, matrix):
        self.grid = matrix
        self.XLIM, self.YLIM = matrix.shape
        self.XLIM -= 1
        self.YLIM -= 1

    def neighbors(self, node):
        x, y = node
        nbrs = [
            (max(x - 1, 0), y),
            (min(x + 1, self.XLIM), y),
            (x, max(y - 1, 0)),
            (x, min(y + 1, self.YLIM)),
        ]

        nbrs = [n for n in nbrs if self.grid[n[0], n[1]] != OBSTACLE]
        return nbrs
