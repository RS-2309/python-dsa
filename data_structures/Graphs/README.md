# Graph Implementations

Graph implementations written from scratch in Python using adjacency lists.

These implementations were created as part of my Data Structures & Algorithms (DSA) learning journey to understand graph traversal, connectivity, graph variants, and graph algorithms.

---

## Files

```text
undirected_graph.py
test_undirected_graph.py

directed_graph.py
test_directed_graph.py

weighted_graph.py
test_weighted_graph.py
```

- **undirected_graph.py** – Implements an undirected graph.
- **directed_graph.py** – Implements a directed graph.
- **weighted_graph.py** – Implements a weighted graph.
- All implementations include corresponding test files.

---

## Implementations

### Undirected Graph

Features:

- Add/Remove vertices
- Add/Remove edges
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Connectivity checks
- BFS caching
- Distance tracking

---

### Directed Graph

Features:

- Add/Remove vertices
- Add/Remove directed edges
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Weak connectivity checks
- Strong connectivity checks
- BFS caching
- Distance tracking

---

### Weighted Graph

Features:

- Add/Remove vertices
- Add/Remove weighted edges
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Connectivity checks
- Weight retrieval
- Weight updates
- Neighbor queries
- BFS caching
- Distance tracking

---

## Graph Variants

| Graph Type | Directed | Weighted |
| ---------- | :------: | :------: |
| Undirected Graph | No | No |
| Directed Graph | Yes | No |
| Weighted Graph | No | Yes |

---

## Python Special Methods

All graph implementations support:

| Method | Purpose |
|------|------|
| `__contains__` | Enables use of `in`. |
| `__len__` | Enables use of `len()`. |
| `__repr__` | Developer-friendly representation. |
| `__str__` | Human-readable graph summary. |
| `__iter__` | Enables iteration over vertices. |
| `__getitem__` | Enables adjacency list access. |

---

## Supported Algorithms

### Traversal

- Breadth First Search (BFS)
- Depth First Search (DFS)

### Connectivity

- Connected Components
- Cycle Detection
- Connectivity Checks
- Weak Connectivity
- Strong Connectivity

### Coming Soon

- Dijkstra's Algorithm
- Topological Sort
- Prim's Algorithm
- Kruskal's Algorithm

---

## Time Complexity

| Operation | Complexity |
|----------|------------|
| Add Vertex | O(1) |
| Remove Vertex | O(V + E) |
| Add Edge | O(1) |
| Remove Edge | O(1) - O(V) |
| BFS | O(V + E) |
| DFS | O(V + E) |
| Connectivity Checks | O(V + E) |

---

## Design Choices

- Implemented using adjacency lists.
- Supports undirected, directed, and weighted graphs.
- BFS results are cached when possible.
- Supports arbitrary string vertex names.
- Supports iteration over vertices.
- Supports adjacency list access using `[]`.
- Duplicate edges are ignored.
- Directed graphs support weak and strong connectivity checks.
- Weighted graphs store weights using dictionaries.

---

## Learning Objectives

This implementation was created to understand:

- Graph representations
- Adjacency Lists
- Breadth First Search
- Depth First Search
- Connected Components
- Cycle Detection
- Weak vs Strong Connectivity
- Weighted Graphs
- Graph Traversal Algorithms
- Complexity Analysis