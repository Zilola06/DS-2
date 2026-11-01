"""Task 1: Breadth-First Search (BFS)"""

#Graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"]
}


def bfs(graph, start):
    #Manual queue: list + front index
    queue = [start]
    front = 0

    #Mark nodes when enqueued to avoid duplicates
    discovered = {start}
    dist = {start: 0}
    parent = {start: None}
    order = []

    while front < len(queue):
        u = queue[front]
        front += 1

        order.append(u)

        #Neighbours are already in alphabetical order
        for v in graph[u]:
            if v not in discovered:
                discovered.add(v)
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    return order, dist, parent


def shortest_path(graph, start, target):
    order, dist, parent = bfs(graph, start)

    #Target is unreachable
    if target not in dist:
        return None, None

    #Rebuild path backwards using parent
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return dist[target], path


#BFS traversal from A
order, dist, parent = bfs(graph, "A")
print("BFS order from A:", " ".join(order))

#Shortest path A -> G
distance, path = shortest_path(graph, "A", "G")
print(
    f"Shortest A -> G: distance {distance}, "
    f"path {' -> '.join(path)}"
)

#Shortest path D -> G
distance, path = shortest_path(graph, "D", "G")
print(
    f"Shortest D -> G: distance {distance}, "
    f"path {' -> '.join(path)}"
)
