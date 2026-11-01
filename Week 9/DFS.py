"""Task 2: Iterative Depth-First Search (DFS)"""

#Graph:
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"]
}


def dfs(graph, start):
    #Explicit stack (LIFO)
    stack = [start]
    visited = set()
    order = []

    while stack:
        u = stack.pop()

        #Skip duplicate copies already visited
        if u in visited:
            continue

        visited.add(u)
        order.append(u)

        #Push neighbours in reverse alphabetical order
        #so the alphabetically first is popped first.
        for v in sorted(graph[u], reverse=True):
            if v not in visited:
                stack.append(v)

    return order


#Run DFS from A and G
print("DFS order from A:", " ".join(dfs(graph, "A")))
print("DFS order from G:", " ".join(dfs(graph, "G")))
