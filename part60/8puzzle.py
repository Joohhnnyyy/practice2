from collections import deque


# Print puzzle in grid format
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Get possible moves
def get_neighbors(state):
    
    neighbors = []
    index = state.index(0)

    row = index // 3
    col = index % 3

    moves = [
        (row-1, col),  # up
        (row+1, col),  # down
        (row, col-1),  # left
        (row, col+1)   # right
    ]

    for r, c in moves:
        if 0 <= r < 3 and 0 <= c < 3:
            
            new_index = r * 3 + c
            new_state = list(state)

            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]

            neighbors.append(tuple(new_state))

    return neighbors


# BFS algorithm
def bfs(start, goal):

    queue = deque()
    queue.append((start, []))

    visited = set()

    while queue:

        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))

    return None


# Initial and goal states
start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


solution = bfs(start_state, goal_state)

print("\nInitial State:\n")
print_puzzle(start_state)

if solution:
    print("Steps to reach Goal State:\n")
    
    for step in solution:
        print_puzzle(step)

else:
    print("No solution found.")