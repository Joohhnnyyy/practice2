import math

def minimax(depth, node_index, maximizing_player, values, max_depth):

    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, values, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, values, max_depth)
        )


values = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = int(math.log2(len(values)))

print("\n========== MINIMAX ALGORITHM ==========\n")

print("Leaf Node Values:")
print(values)

optimal_value = minimax(0, 0, True, values, max_depth)

print("\n---------------------------------------")
print("Optimal Value Computed by Minimax:", optimal_value)
print("---------------------------------------")
