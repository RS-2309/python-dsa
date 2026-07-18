from data_structures.Graphs.undirected_graph import UndirectedGraph

def connected_components(graph: UndirectedGraph) -> list:
    """
    Returns a list of connected components.
    """
    connected_components_list = []
    visited = set()

    for key in graph:
        if key not in visited:
            result = graph.bfs(key)
            connected_components_list.append(result.order)
            visited.update(result.order)

    return connected_components_list