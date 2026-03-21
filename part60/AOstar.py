# AO* Algorithm Implementation

# AND-OR graph representation
graph = {
    'A': [['B', 'C'], ['D']],     # A -> (B AND C) OR (D)
    'B': [['E'], ['F']],          # B -> E OR F
    'C': [['G']],                 # C -> G
    'D': [['H']],                 # D -> H
}

# Initial heuristic values
heuristic = {
    'A': 10,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 6,
    'F': 8,
    'G': 2,
    'H': 0
}

solution = {}


def ao_star(node):

    # If node is a terminal node
    if node not in graph:
        return heuristic[node]

    min_cost = float('inf')
    best_children = None

    # Explore all AND/OR options
    for child_group in graph[node]:

        cost = 0
        for child in child_group:
            cost += ao_star(child)

        if cost < min_cost:
            min_cost = cost
            best_children = child_group

    heuristic[node] = min_cost
    solution[node] = best_children

    return heuristic[node]


# Solve starting from root node
start = 'A'
ao_star(start)

print("\nOptimal Solution Graph:\n")

for node in solution:
    print(node, "->", solution[node])