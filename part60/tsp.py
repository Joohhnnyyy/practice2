import random

# City names
cities = ["A", "B", "C", "D"]

# Distance matrix
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


# Convert route numbers to city names
def route_to_cities(route):
    return " -> ".join(cities[i] for i in route) + " -> " + cities[route[0]]


# Calculate route distance
def calculate_distance(route):

    total = 0

    for i in range(len(route) - 1):
        total += distances[route[i]][route[i + 1]]

    total += distances[route[-1]][route[0]]

    return total


# Generate neighboring route
def get_neighbor(route):

    new_route = route[:]

    i, j = random.sample(range(len(route)), 2)

    new_route[i], new_route[j] = new_route[j], new_route[i]

    return new_route


# Hill Climbing Algorithm
def hill_climbing():

    current_route = list(range(len(cities)))
    random.shuffle(current_route)

    current_cost = calculate_distance(current_route)

    print("\n========== Travelling Salesman Problem ==========\n")

    print("Initial Route:")
    print(route_to_cities(current_route))
    print("Initial Distance:", current_cost)

    print("\nSearching for better route...\n")

    while True:

        neighbor = get_neighbor(current_route)
        neighbor_cost = calculate_distance(neighbor)

        if neighbor_cost < current_cost:
            current_route = neighbor
            current_cost = neighbor_cost

    # Stop when no better neighbor
        else:
            break

    print("========== Optimal Solution Found ==========\n")

    print("Best Route:")
    print(route_to_cities(current_route))

    print("\nMinimum Distance:", current_cost)

    print("\n=============================================")


hill_climbing()