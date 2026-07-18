# Graph

An undirected graph implementation written from scratch in Python using an adjacency list.

This implementation was created as part of my Data Structures & Algorithms (DSA) learning journey to understand graph traversal, connectivity, and graph manipulation algorithms.

---

## Files

```text
graph.py
test_graph.py
```

- **graph.py** – Contains the `Graph` implementation and BFS result class.
- **test_graph.py** – Demonstrates and tests all implemented operations.

---

## Features

- Add vertices
- Remove vertices
- Add edges
- Remove edges
- Check connectivity
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Membership testing using `in`
- Cached BFS results
- Distance tracking using BFS

---

## Supported Operations

| Method | Description |
|-------|------|
| `add_vertex()` | Adds a vertex to the graph. |
| `remove_vertex()` | Removes a vertex and all connected edges. |
| `add_edge()` | Adds an undirected edge between two vertices. |
| `remove_edge()` | Removes an edge between two vertices. |
| `has_vertex()` | Checks if a vertex exists. |
| `has_edge()` | Checks if an edge exists. |
| `bfs()` | Performs Breadth First Search. |
| `dfs()` | Performs Depth First Search. |
| `is_connected()` | Checks whether the graph is connected. |

---

## Python Special Methods

| Method | Purpose |
|------|------|
| `__contains__` | Enables use of `in`. |
| `__len__` | Enables use of `len()`. |
| `__repr__` | Developer-friendly representation. |
| `__str__` | Human-readable graph summary. |

---

## Example

```python
graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

graph.add_edge("A", "B")
graph.add_edge("B", "C")

print(graph.bfs("A").order)

# ['A', 'B', 'C']
```

---

## BFS Result Object

`bfs()` returns a `BFSResult` object containing:

```python
result = graph.bfs("A")

result.order
result.place_value
```

Example:

```python
Order:
['A', 'B', 'C']

Distances:
{
    'A': 0,
    'B': 1,
    'C': 2
}
```

---

## Time Complexity

| Operation | Complexity |
|----------|------------|
| Add Vertex | O(1) |
| Remove Vertex | O(V + E) |
| Add Edge | O(1) |
| Remove Edge | O(V) |
| Has Vertex | O(1) |
| Has Edge | O(V) |
| BFS | O(V + E) |
| DFS | O(V + E) |
| Connectivity Check | O(V + E) |

---

## Design Choices

- Implemented using adjacency lists.
- Graph is undirected.
- BFS results are cached when possible.
- BFS tracks the shortest distance from the start node.
- Supports arbitrary string vertex names.
- Duplicate edges are ignored.

---

## Learning Objectives

This implementation was created to understand:

- Graph representations
- Adjacency Lists
- Breadth First Search
- Depth First Search
- Graph connectivity
- Shortest path distances using BFS
- Graph traversal algorithms
- Complexity analysis