def bellman_ford(nodes, edges, start_node):
    """
    Finds the shortest path from start_node and detects negative cycles.
    nodes: A list of all node keys (e.g., ['A', 'B', 'C'])
    edges: A list of all edges (u, v, weight)
    """
    # distances: {node: shortest_distance_from_start}
    distances = {node: float('inf') for node in nodes}      #nodes = ['A', 'B', 'C'], {'A': inf, 'B': inf, 'C': inf}
    distances[start_node] = 0
    num_nodes = len(nodes)

    # Relax all edges |V| - 1 times
    for i in range(num_nodes - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative cycles (V-th iteration)
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return "Graph contains a negative weight cycle."

    return distances

# Example usage (Same as Dijkstra's, but Bellman-Ford can handle negative weights)
# nodes = ['A', 'B', 'C', 'D']
# edges = [
#     ('A', 'B', 1), ('A', 'C', 4),
#     ('B', 'C', 2), ('B', 'D', 5),
#     ('C', 'D', 1)
# ]
# print(f"Bellman-Ford distances from A: {bellman_ford(nodes, edges, 'A')}")
# Expected: {'A': 0, 'B': 1, 'C': 3, 'D': 4}