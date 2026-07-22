from directed_graphs import DirectedGraph

print("========== DIRECTED GRAPH TEST ==========\n")

# Constructor
graph = DirectedGraph()

print("Empty graph created.")
print("Vertices:", len(graph))
print("Weakly Connected:", graph.is_weakly_connected())
print("Strongly Connected:", graph.is_strongly_connected())
print()

# Add Vertices
print("Adding vertices...")

vertices = ["A", "B", "C", "D", "E"]

for vertex in vertices:
    graph.add_vertex(vertex)

print(graph)
print()

# Iteration
print("Testing Iteration")

for vertex in graph:
    print(vertex, end=" ")

print("\n")

# Add Edges
print("Adding directed edges...")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")
graph.add_edge("D", "E")

print(graph)
print()

# Adjacency Access
print("Testing __getitem__")
print("Neighbors of A:", graph["A"])
print("Neighbors of D:", graph["D"])
print()

# Membership
print("Membership Tests")
print("'A' in graph:", "A" in graph)
print("'Z' in graph:", "Z" in graph)
print()

# Vertex / Edge Checks
print("Vertex Checks")
print("Has Vertex A:", graph.has_vertex("A"))
print("Has Vertex Z:", graph.has_vertex("Z"))
print()

print("Edge Checks")
print("A -> B:", graph.has_edge("A", "B"))
print("B -> A:", graph.has_edge("B", "A"))
print()

# BFS
print("Breadth First Search")

bfs_result = graph.bfs("A")

print("Traversal Order:")
print(bfs_result.order)

print("\nDistances:")
print(bfs_result.place_value)

print()

# DFS
print("Depth First Search")
print(graph.dfs("A"))
print()

# Connectivity
print("Connectivity")
print("Weakly Connected:", graph.is_weakly_connected())
print("Strongly Connected:", graph.is_strongly_connected())
print()

# Remove Edge
print("Removing edge (D -> E)...")

graph.remove_edge("D", "E")

print(graph)
print()

# Remove Vertex
print("Removing vertex E...")

graph.remove_vertex("E")

print(graph)
print()

# Connectivity Again
print("Connectivity After Changes")
print("Weakly Connected:", graph.is_weakly_connected())
print("Strongly Connected:", graph.is_strongly_connected())
print()

# Testing NotImplemented
print("Testing is_connected()")

try:
    graph.is_connected()
except NotImplementedError as e:
    print(type(e).__name__ + ":", e)

print()

# Exception Tests
print("Testing Exceptions")

try:
    graph.add_edge("A", "X")
except KeyError as e:
    print("KeyError:", e)

try:
    graph.remove_vertex("X")
except KeyError as e:
    print("KeyError:", e)

try:
    graph.remove_edge("A", "X")
except KeyError as e:
    print("KeyError:", e)

try:
    print(graph["X"])
except KeyError as e:
    print("KeyError:", e)

print()

# Strongly Connected Graph
print("Testing Strong Connectivity")

g2 = DirectedGraph()

for vertex in ["X", "Y", "Z"]:
    g2.add_vertex(vertex)

g2.add_edge("X", "Y")
g2.add_edge("Y", "Z")
g2.add_edge("Z", "X")

print(g2)
print("Weakly Connected:", g2.is_weakly_connected())
print("Strongly Connected:", g2.is_strongly_connected())
print()

print("========== TEST COMPLETE ==========")