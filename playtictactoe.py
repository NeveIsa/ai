from search.adversarial import minimax
from games.tictactoe import Game
import numpy as np

game = Game()
state = np.zeros((3, 3))

while True:
    val, action = minimax(game, state)

    # print("ok", action)
    state = game.result(state, (1, action))
    print(state, "\n")

    x, y = [int(a) for a in input().split(" ")]
    state[x, y] = -1

    print(state)
