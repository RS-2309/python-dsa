import heapq
from data_structures.Graphs.weighted_graph import WeightedGraph

def dijkstra(graph: WeightedGraph, start: str):

    if start not in graph:
        raise KeyError(start)

    distances = {
        vertex: float("inf")
        for vertex in graph
    }

    previous = {
        vertex: None
        for vertex in graph
    }

    distances[start] = 0

    heap = [(0, start)]

    while heap:

        distance, current = heapq.heappop(heap)

        if distance > distances[current]:
            continue

        for neighbor, weight in graph[current].items():

            candidate = distance + weight

            if candidate < distances[neighbor]:

                distances[neighbor] = candidate
                previous[neighbor] = current

                heapq.heappush(heap, (candidate, neighbor))

    return distances, previous

def build_path(previous, destination):

    if destination not in previous:
        raise KeyError(destination)

    path = []

    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path