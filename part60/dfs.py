# Maze representation
# 1 = path
# 0 = blocked

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

N = 4


def print_maze(grid, title):
    print("\n" + title)
    print("-" * 25)
    for row in grid:
        for cell in row:
            print(cell, end="  ")
        print()
    print("-" * 25)


def print_solution(solution):
    print("\nSolution Path ( * = path )")
    print("-" * 25)

    for i in range(N):
        for j in range(N):
            if solution[i][j] == 1:
                print("*", end="  ")
            else:
                print(".", end="  ")
        print()

    print("-" * 25)


def is_safe(x, y):

    if 0 <= x < N and 0 <= y < N and maze[x][y] == 1:
        return True

    return False


def solve_maze(x, y, solution):

    # Destination reached
    if x == N - 1 and y == N - 1:
        solution[x][y] = 1
        return True

    if is_safe(x, y):

        solution[x][y] = 1

        # Move Down
        if solve_maze(x + 1, y, solution):
            return True

        # Move Right
        if solve_maze(x, y + 1, solution):
            return True

        # Backtracking
        solution[x][y] = 0
        return False

    return False


# Solution matrix
solution = [[0 for _ in range(N)] for _ in range(N)]

print_maze(maze, "Original Maze (1 = path, 0 = blocked)")

if solve_maze(0, 0, solution):

    print_solution(solution)

else:
    print("\nNo path exists in the maze.")