from collections import deque


def water_jug_bfs(jug1_capacity, jug2_capacity, target):

    visited = set()
    queue = deque()

    # Initial state (both jugs empty)
    queue.append((0, 0))

    print("Steps to reach the target:\n")

    while queue:

        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        print("Jug1:", jug1, " Jug2:", jug2)

        # Check if target is reached
        if jug1 == target or jug2 == target:
            print("\nTarget achieved!")
            return

        # Possible operations

        # Fill Jug1
        queue.append((jug1_capacity, jug2))

        # Fill Jug2
        queue.append((jug1, jug2_capacity))

        # Empty Jug1
        queue.append((0, jug2))

        # Empty Jug2
        queue.append((jug1, 0))

        # Pour Jug1 -> Jug2
        transfer = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - transfer, jug2 + transfer))

        # Pour Jug2 -> Jug1
        transfer = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + transfer, jug2 - transfer))


# Example
jug1 = 4
jug2 = 3
target = 2

water_jug_bfs(jug1, jug2, target)