import plotext as plt
from time import sleep
from numpy import zeros
import numpy as np


def animate(G, visitorder):
    n = np.sqrt(len(G.nodes))
    n = int(n)
    m = zeros((n, n)).tolist()

    delta = 1 / n / n
    for x, y in visitorder:
        m[x][y] = 1
        plt.matrix_plot(m)
        plt.plotsize(200, 100)
        plt.show()
        sleep(delta)
        plt.clf()
