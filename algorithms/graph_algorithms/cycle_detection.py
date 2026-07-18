from data_structures.Graphs.undirected_graph import UndirectedGraph

def cycle_detection(graph: UndirectedGraph) -> bool:
    visited_graph = set()

    for key in graph:
        visited_graph.update(visited)
        if key not in visited_graph:
            stack = [(key, None)]
            visited = set()
            
            while stack:
                current, parent = stack.pop()

                if current in visited:
                    continue

                visited.add(current)

                for neighbor in reversed(graph[current]):
                    if neighbor not in visited:
                        stack.append((neighbor, current))

                    if neighbor in visited and neighbor != parent:
                        return True

    return False