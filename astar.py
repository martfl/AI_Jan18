from functools import reduce

class Node:
    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.heuristic = -1


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


def a_star(initial, final, heuristic):
    nodes = [Node(initial, None, None, 0)]
    cycle = 0
    while nodes:
        for node in nodes:
            node.heuristic = node.depth + heuristic(node.state, final)
        
        node = reduce(lambda smallest, current: smallest if (smallest.heuristic < current.heuristic) else current, nodes)
        #node = nodes.pop(0)

        if node.state == final:
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.action)
                if temp.depth == 1: 
                    break
                temp = temp.parent
            return moves
        nodes = make_moves(node)
        cycle += 1
        if cycle == 100000:
            return None
    return None


def manhattan(state, final):
    distance = 0
    for i in range(len(state)):
        if state[i] != 0:
            row = int(final.index(state[i]) / 3)
            col = final.index(state[i]) % 3
            distance += abs(row - int(i / 3)) + abs(col - (i % 3))
    return distance


def hamming(state, final):
    distance = 0
    for i in range(len(state)):
        if state[i] != final[i] and state[i] != 0:
            distance += 1
        i += 1
    return distance


def main():
    print("Enter the initial state (row wise): ")
    print("e.g. 120453786\n")
    print_board([1, 2, 0, 4, 5, 3, 7, 8, 6])
    state = list(map(int, input()))
    print("Enter 'asm'(Manhattan) or 'aso'(Out-of-place) for heuristic(defaults to 'asm'): ")
    heuristic = input()
    final_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    if heuristic == 'aso':
        result = a_star(state, final_state, hamming)
    else:
        result = a_star(state, final_state, manhattan)
    print("Initial state")
    print_board(state)
    print("Final state")
    print_board(final_state)

    if result is None:
        print("\nNo solution found\n")
    else:
        print(result)
        print(len(result), " moves")


if __name__ == "__main__":
    main()
