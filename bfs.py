from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited)

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
    print("Breadth-First Search (BFS)")
    graph = create_graph()
    start_node = input("Enter the starting node: ")

    if start_node in graph:
        print("Breadth-First Traversal:")
        bfs(graph, start_node)
    else:
        print("Starting node not found in the graph.")

if __name__ == "__main__":
    main()
