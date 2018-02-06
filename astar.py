class Node:
    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth


def print_board(state):
    print("%i  %i  %i" % (state[0], state[1], state[2]))
    print("%i  %i  %i" % (state[3], state[4], state[5]))
    print("%i  %i  %i" % (state[6], state[7], state[8]))
    print("")


def move(state, move_dir):
    next_state = state[:]
    i = next_state.index(0)
    if move_dir == 'l':
        if i not in [0, 3, 6]:
            next_state[i - 1], next_state[i] = next_state[i], next_state[i - 1]
            return next_state
        else:
            return None
    elif move_dir == 'r':
        if i not in [2, 5, 8]:
            next_state[i + 1], next_state[i] = next_state[i], next_state[i + 1]
            return next_state
        else:
            return None
    elif move_dir == 'u':
        if i not in [0, 1, 2]:
            next_state[i - 3], next_state[i] = next_state[i], next_state[i - 3]
            return next_state
        else:
            return None
    elif move_dir == 'd':
        if i not in [6, 7, 8]:
            next_state[i + 3], next_state[i] = next_state[i], next_state[i + 3]
            return next_state
        else:
            return None


def make_moves(node):
    exp_nodes = [Node(move(node.state, 'u'), node, 'u', node.depth + 1),
                 Node(move(node.state, 'd'), node, 'd', node.depth + 1),
                 Node(move(node.state, 'l'), node, 'l', node.depth + 1),
                 Node(move(node.state, 'r'), node, 'r', node.depth + 1)]
    exp_nodes = [node for node in exp_nodes if node.state is not None]
    return exp_nodes


def dfs(initial, final, max_depth):
    nodes = [Node(initial, None, None, 0)]
    while nodes:
        node = nodes.pop(0)
        if node.state == final:
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.action)
                if temp.depth <= 1: break
                temp = temp.parent
            return moves
        if node.depth < max_depth:
            exp_nodes = make_moves(node)
            exp_nodes.extend(nodes)
            nodes = exp_nodes
    return None


def bfs(initial, final):
    nodes = [Node(initial, None, None, 0)]
    while nodes:
        node = nodes.pop(0)
        if node.state == final:
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.action)
                if temp.depth == 1: break
                temp = temp.parent
            return moves
        nodes.extend(make_moves(node))
    return None


def main():
    print("Enter the initial state (row wise): ")
    print("e.g. 120453786")
    print_board([1, 2, 0, 4, 5, 3, 7, 8, 6])
    state = list(map(int, input()))
    print("Enter 'dfs' or 'bfs' for search algorithm (defaults to dfs): ")
    algo = input()
    final_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    if algo == 'bfs':
        result = bfs(state, final_state)
    else:
        print("Enter max depth (defaults to 15): ")
        depth = input()
        try:
            int(depth)
        except ValueError:
            depth = 15
        result = dfs(state, final_state, depth)
    print("Final state")
    print_board(final_state)
    print("Initial state")
    print_board(state)
    if result is None:
        print("\nNo solution found\n")
    else:
        print(result)
        print(len(result), " moves")


if __name__ == "__main__":
    main()
