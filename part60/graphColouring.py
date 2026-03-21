V = 4

graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

colors = ["Red", "Green", "Blue", "Yellow"]
solution = [0] * V


def is_safe(node, color):

    for i in range(V):
        if graph[node][i] == 1 and solution[i] == color:
            return False

    return True


def graph_coloring(node):

    if node == V:
        return True

    for color in range(1, len(colors)+1):

        if is_safe(node, color):

            solution[node] = color

            if graph_coloring(node+1):
                return True

            solution[node] = 0

    return False


print("\n========== GRAPH COLORING PROBLEM ==========\n")

print("Graph Adjacency Matrix")
print("------------------------------------")

for row in graph:
    print(row)

if graph_coloring(0):

    print("\nColor Assignment")
    print("------------------------------------")

    for i in range(V):
        print(f"Vertex {i}  --->  {colors[solution[i]-1]}")

    print("\n============================================")

else:
    print("No solution exists")