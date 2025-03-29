from game import Game


class TicTacToe(Game):
    def statezero(self, initboard="-" * 9, turn="x"):
        state = {"board": initboard, "turn": turn}
        return state

    def actions(self, state):
        empty = [i for i, x in enumerate(state["board"]) if x == " "]
        return empty

    def result(self, state, action):
        assert 0 <= action < 9
        result = (
            state.copy()
        )  # this only works because board and turn are strings and hence immutable
        result["board"][action] = state["turn"]
        result["turn"] = "x" if state["turn"] == "o" else "o"

        return result

    def is_terminal(self, state):
        return " " not in state["board"]

    def utility(self, state, player):
        winpos = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (6, 4, 2),
        ]

        board = state["board"]
        for pos in winpos:
            a, b, c = pos
            if board[a] == board[b] == board[c]:
                winner = board[a]
            else:
                winner = ""

        if winner == "":
            return 0
        elif winner == player:
            return +1
        else:
            return -1

    def to_move(self, state):
        return state["turn"]

    def display(self, state):
        board = state["board"]
        turn = state["turn"]

        print()
        print(" ".join(board[:3]))
        # print("-" * 5)
        print(" ".join(board[3:6]))
        # print("-" * 5)
        print(" ".join(board[6:]))
        # print("-" * 5)
        print("TURN:", turn)
        print()


if __name__ == "__main__":
    ttt = TicTacToe()
    state = ttt.statezero()
    ttt.display(state)
