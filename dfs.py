def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)

def create_graph():
    graph = {}
    while True:
        edge = input("Enter an edge (e.g., A B), or press Enter to finish: ")
        if not edge:
            break
        node1, node2 = edge.split()
        graph.setdefault(node1, []).append(node2)
        graph.setdefault(node2, []).append(node1)
    return graph

def main():
    print("Depth-First Search (DFS)")
    graph = create_graph()
    start_node = input("Enter the starting node: ")

    if start_node in graph:
        print("Depth-First Traversal:")
        visited = set()
        dfs(graph, start_node, visited)
    else:
        print("Starting node not found in the graph.")

if __name__ == "__main__":
    main()
