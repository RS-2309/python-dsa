from weighted_graph import WeightedGraph

print("========== WEIGHTED GRAPH TEST ==========\n")

graph = WeightedGraph()

print("Empty graph created.")
print("Vertices:", len(graph))
print("Connected:", graph.is_connected())
print()

print("Adding vertices...")

for vertex in ["A", "B", "C", "D", "E"]:
    graph.add_vertex(vertex)

print(graph)
print()

print("Adding weighted edges...")

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "D", 7)
graph.add_edge("C", "D", 1)
graph.add_edge("D", "E", 3)

print(graph)
print()

print("Testing weights...")
print("A-B:", graph.get_weight("A", "B"))
print("C-D:", graph.get_weight("C", "D"))
print()

print("Updating weight...")
graph.update_weights("A", "B", 10)

print("A-B:", graph.get_weight("A", "B"))
print()

print("Testing neighbors...")
print(list(graph.neighbors("D")))
print()

print("Testing BFS...")
result = graph.bfs("A")

print(result.order)
print(result.place_value)
print()

print("Testing DFS...")
print(graph.dfs("A"))
print()

print("Testing Connectivity...")
print(graph.is_connected())
print()

print("Removing edge (D, E)...")
graph.remove_edge("D", "E")

print(graph)
print()

print("Removing vertex E...")
graph.remove_vertex("E")

print(graph)
print()

print("Testing Exceptions")

tests = [
    lambda: graph.get_weight("A", "X"),
    lambda: graph.neighbors("X"),
    lambda: graph.remove_vertex("X"),
    lambda: graph.remove_edge("A", "X")
]

for test in tests:
    try:
        test()
    except Exception as e:
        print(type(e).__name__, ":", e)

print()

print("Testing disconnected graph...")

g2 = WeightedGraph()

g2.add_vertex("X")
g2.add_vertex("Y")
g2.add_vertex("Z")

g2.add_edge("X", "Y", 5)

print(g2)
print("Connected:", g2.is_connected())

print("\n========== TEST COMPLETE ==========")