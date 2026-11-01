"""Task 3: Dijkstra's Algorithm"""

#Graph
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3}
}

def dijkstra(graph, source):
    #Initialize distances and previous nodes
    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    settled = set()

    dist[source] = 0

    def print_distances():
        print(" ".join(
            f"{node}={dist[node] if dist[node] != float('inf') else 'INF'}"
            for node in sorted(graph)
        ))

    print("init          |", end=" ")
    print_distances()

    while True:
        #Find unsettled node with the smallest distance
        u = None
        for node in graph:
            if node not in settled:
                if u is None or dist[node] < dist[u]:
                    u = node

        #Stop if remaining nodes are unreachable
        if u is None or dist[u] == float("inf"):
            break

        settled.add(u)

        # Relax edges to unsettled neighbours
        for v, weight in graph[u].items():
            if v not in settled:
                new_dist = dist[u] + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u

        print(f"settle {u} ({dist[u]}) |", end=" ")
        print_distances()

    return dist, prev

def reconstruct_path(prev, source, target):
    if target != source and prev[target] is None:
        return None

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()
    return path

#Run Dijkstra from A
dist, prev = dijkstra(graph, "A")

#Print cheapest paths to every other node
for target in sorted(graph):
    if target == "A":
        continue

    path = reconstruct_path(prev, "A", target)

    if path is None:
        print(f"A to {target}: no path")
    else:
        print(
            f"A to {target}: cost {dist[target]}: "
            f"{' -> '.join(path)}"
        )
