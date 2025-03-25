from queue import LifoQueue as LIFO
from queue import SimpleQueue as FIFO
from queue import PriorityQueue as PQUE


def wrapper(Stack):
    def traverse(G, start, goalfn=lambda x: False):
        """
        G : A graph object that has neighbors function as in NetworkX library
        start: start node
        """
        visits = []  # store the order of visits
        visitedset = (
            set()
        )  # it is O(1) to check it element present vs a list which takes O(n)
        stack = Stack()

        stack.put(start)  # push the start node
        while not stack.empty():  # while not empty
            node = stack.get()
            if node in visitedset:  # check if already visited
                continue
            else:
                visits += [node]  # append
                visitedset |= {node}  # add to set

                if goalfn(node):  # if hit goal, return
                    break

                for nbr in G.neighbors(node):
                    stack.put(nbr)

        return visits

    return traverse


dfs = wrapper(Stack=LIFO)
bfs = wrapper(Stack=FIFO)
bestfs = wrapper(Stack=PQUE)
