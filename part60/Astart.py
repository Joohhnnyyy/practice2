import heapq


# Print puzzle in grid format
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Manhattan Distance Heuristic
def heuristic(state, goal):

    distance = 0

    for i in range(1, 9):

        current_index = state.index(i)
        goal_index = goal.index(i)

        x1, y1 = divmod(current_index, 3)
        x2, y2 = divmod(goal_index, 3)

        distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate neighbors
def get_neighbors(state):

    neighbors = []
    index = state.index(0)

    row, col = divmod(index, 3)

    moves = [
        (row-1, col),
        (row+1, col),
        (row, col-1),
        (row, col+1)
    ]

    for r, c in moves:

        if 0 <= r < 3 and 0 <= c < 3:

            new_index = r * 3 + c
            new_state = list(state)

            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]

            neighbors.append(tuple(new_state))

    return neighbors


# A* Algorithm
def a_star(start, goal):

    priority_queue = []

    heapq.heappush(priority_queue, (0, start, []))

    visited = set()

    while priority_queue:

        cost, state, path = heapq.heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):

            g = len(path) + 1
            h = heuristic(neighbor, goal)

            f = g + h

            heapq.heappush(priority_queue, (f, neighbor, path + [state]))

    return None


# Initial and goal states
start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


solution = a_star(start_state, goal_state)

print("\nInitial State:\n")
print_puzzle(start_state)

if solution:

    print("Steps to reach Goal State:\n")

    step = 0

    for state in solution:
        print("Step", step)
        print_puzzle(state)
        step += 1

else:
    print("No solution found.")