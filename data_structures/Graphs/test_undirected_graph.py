from undirected_graph import UndirectedGraph

print("========== UNDIRECTED GRAPH TEST ==========\n")

# Constructor
graph = UndirectedGraph()

print("Empty graph created.")
print("Vertices:", len(graph))
print("Connected:", graph.is_connected())
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
print("Adding edges...")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")

print(graph)
print()

# Adjacency List Access
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
print("A-B:", graph.has_edge("A", "B"))
print("A-E:", graph.has_edge("A", "E"))
print()

# BFS
print("Breadth First Search")

bfs_result = graph.bfs("A")

print("Traversal Order:")
print(bfs_result.order)

print("\nDistances:")
print(bfs_result.place_value)

print("\nMembership on BFSResult")
print("D in BFS:", "D" in bfs_result)
print("X in BFS:", "X" in bfs_result)

print()

# Cached BFS
print("Testing BFS Cache")
print(graph.bfs("A"))
print()

# DFS
print("Depth First Search")
print(graph.dfs("A"))
print()

# Connectivity
print("Connectivity")
print("Connected:", graph.is_connected())
print()

# Remove Edge
print("Removing edge (C, D)...")
graph.remove_edge("C", "D")

print(graph)
print()

# Remove Vertex
print("Removing vertex E...")
graph.remove_vertex("E")

print(graph)
print()

# Connectivity After Changes
print("Connectivity After Changes")
print("Connected:", graph.is_connected())
print()

# Exception Tests
print("Testing Exceptions")

try:
    graph.add_edge("A", "Z")
except KeyError as e:
    print("KeyError:", e)

try:
    graph.remove_vertex("X")
except KeyError as e:
    print("KeyError:", e)

try:
    graph.remove_edge("A", "E")
except KeyError as e:
    print("KeyError:", e)

try:
    graph.has_edge("A", "X")
except KeyError as e:
    print("KeyError:", e)

try:
    print(graph["X"])
except KeyError as e:
    print("KeyError:", e)

print()

# Disconnected Graph
print("Testing Disconnected Graph")

g2 = UndirectedGraph()

for vertex in ["X", "Y", "Z"]:
    g2.add_vertex(vertex)

g2.add_edge("X", "Y")

print(g2)
print("Connected:", g2.is_connected())
print()

print("========== TEST COMPLETE ==========")