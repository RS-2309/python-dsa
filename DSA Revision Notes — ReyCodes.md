# DSA Revision Notes

A personal reference for concepts already learned and implemented.

The goal is **understanding + recall**, not memorizing implementations.

---

# 1. Arrays

## What is an array?

An array stores elements in contiguous memory locations.

The important property is that, given an index, we can directly calculate where the element lives.

```python
arr = [10, 20, 30, 40]
```

`arr[2]` directly accesses `30`.

### Why is indexing O(1)?

The computer doesn't search for the element.

Conceptually:

```text
address of arr[i]
= starting address + (i × element size)
```

So accessing any index takes essentially the same amount of work.

## Typical complexities

| Operation | Complexity |
|---|---:|
| Access by index | O(1) |
| Search | O(n) |
| Append (dynamic array, amortized) | O(1) |
| Insert at beginning | O(n) |
| Delete from beginning | O(n) |

The expensive part of inserting/deleting near the beginning is shifting elements.

---

# 2. Strings

A string is essentially a sequence of characters.

```python
s = "hello"
```

Indexing:

```python
s[1]       # 'e'
```

Many string problems become array problems with characters.

Important patterns you've encountered include:

- Two pointers
- Sliding windows
- Character frequency using hash tables
- Building/reversing strings

Your LeetCode work on **Longest Substring Without Repeating Characters** is a classic example of combining strings with a hash-based structure and a moving window.

---

# 3. Linked Lists

## Mental model

An array stores elements next to each other.

A linked list stores **nodes**, where each node knows where the next node is.

```text
[10 | next] → [20 | next] → [30 | None]
```

A node can be represented as:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

## Why use one?

Linked lists make insertion/removal at a known node extremely convenient because we can change pointers instead of shifting an entire array.

But random access is bad.

```python
arr[500]       # O(1)
```

For a linked list:

```text
head → node → node → node → ... → node 500
```

You must walk through the nodes.

So access is O(n).

## Core idea

The important thing isn't the Node class.

It's the **links**.

For:

```text
A → B → C
```

if we want to remove B:

```text
A.next = C
```

and B is no longer part of the chain.

---

# 4. Stack

A stack follows:

> **LIFO — Last In, First Out**

Think of plates:

```text
    C  ← remove first
    B
    A
```

Core operations:

```text
push → put something on top
pop  → remove the top
peek → look at the top
```

Typical complexity:

```text
push  O(1)
pop   O(1)
peek  O(1)
```

## Why stacks matter

Stacks naturally appear whenever the most recently encountered thing must be processed first.

Examples:

- Function call stacks
- Undo operations
- Parentheses matching
- DFS
- Expression conversion/evaluation

---

# 5. Queue

A queue follows:

> **FIFO — First In, First Out**

Think of a line:

```text
A → B → C → D
↑           ↑
front       back
```

A enters first, so A leaves first.

Core operations:

```text
enqueue → add at back
dequeue → remove from front
```

With Python's `deque`:

```python
from collections import deque

queue = deque()

queue.append("A")
queue.append("B")

queue.popleft()
```

Both operations are O(1).

## Why not use a normal list for BFS?

This:

```python
queue.pop(0)
```

requires shifting the remaining elements.

That makes repeated front-removal expensive.

`deque.popleft()` is designed for this job.

---

# 6. Hash Tables

A hash table stores key-value associations.

```python
table = {
    "Alice": 91,
    "Bob": 84
}
```

The important idea is:

```text
key
 ↓
hash function
 ↓
location
 ↓
value
```

This allows average O(1) insertion, lookup, and deletion.

## Why you've used them so much

Hash tables are useful when the problem is essentially:

> "Have I seen this before?"

or:

> "What value is associated with this key?"

Examples:

- Frequency counting
- Duplicate detection
- Two Sum
- Visited sets in graphs
- Memoization

A Python `dict` and `set` are hash-table-based structures.

---

# 7. Binary Search

## What problem does it solve?

Searching a **sorted** collection efficiently.

Suppose:

```text
1  3  5  7  9  11  15
```

Instead of checking from left to right, inspect the middle.

If the target is larger than the middle:

```text
discard left half
```

If smaller:

```text
discard right half
```

Each step eliminates roughly half the remaining possibilities.

Therefore:

```text
O(log n)
```

## The core loop

```python
low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1
```

### The important idea

Binary search is **not a BST**.

A BST is a data structure.

Binary search is a search strategy applied to a sorted sequence.

---

# 8. Median of Two Sorted Arrays

This was the monster.

The key idea is to divide both arrays so that everything on the left represents the lower half of the combined sorted array.

Let:

```text
A | B
```

and:

```text
C | D
```

We want:

```text
A + B + C + D
```

with the partition positioned so that the left side contains exactly half the elements.

We choose a partition in the smaller array.

If the smaller array's partition is `i`, then the other partition is determined:

```python
j = half - i - 2
```

The important condition is:

```text
A_left <= B_right
B_left <= A_right
```

When both are true, the partition is correct.

For an even number of total elements:

```text
median = (max(A_left, B_left) + min(A_right, B_right)) / 2
```

For an odd number:

```text
median = min(A_right, B_right)
```

## Why binary search?

If:

```text
A_left > B_right
```

we put too many elements from A on the left.

Move A's partition left.

If:

```text
B_left > A_right
```

we need more elements from A on the left.

Move A's partition right.

That is the binary-search decision.

Complexity:

```text
O(log(min(m, n)))
```

because we only binary-search the smaller array.

---

# 9. Graphs

A graph consists of:

```text
vertices (nodes)
+
edges (connections)
```

Example:

```text
A —— B
|    |
C —— D
```

## Adjacency list

Your implementation uses dictionaries:

```python
graph = {
    "A": {"B": 5, "C": 2},
    "B": {"A": 5},
    "C": {"A": 2}
}
```

For an unweighted graph:

```python
graph = {
    "A": {"B", "C"},
    "B": {"A"},
    "C": {"A"}
}
```

The adjacency list stores each vertex's neighbors.

---

# 10. BFS

## What problem does BFS solve?

BFS explores a graph **level by level**.

Start:

```text
A
```

Then everything one edge away:

```text
B C
```

Then everything two edges away:

```text
D E F
```

Then the next layer.

Mental model:

> **Spread outward from the starting point.**

## Why does BFS use a queue?

Because we need to process vertices in the same order that we discovered their levels.

Example:

```text
        A
       / \
      B   C
     / \   \
    D   E   F
```

Start:

```text
queue = [A]
```

Process A:

```text
queue = [B, C]
```

Process B:

```text
queue = [C, D, E]
```

Process C:

```text
queue = [D, E, F]
```

Notice what happened.

We completely processed the current layer before moving deeper.

That's exactly what FIFO gives us.

## Canonical implementation

```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    order = []

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return order
```

### What each important part does

```python
queue = deque([start])
```

The next vertex to process.

```python
visited = set()
```

Prevents us from processing the same vertex repeatedly.

```python
current = queue.popleft()
```

Take the oldest discovered vertex.

```python
for neighbor in graph[current]:
```

Look at everything directly connected to it.

```python
queue.append(neighbor)
```

Those vertices will be processed later, after already-discovered vertices.

## BFS and shortest paths

In an **unweighted graph**, BFS also gives the shortest number of edges from the starting vertex.

Why?

Because BFS processes:

```text
distance 0
then distance 1
then distance 2
then distance 3
...
```

It cannot reach a distance-3 vertex before processing the distance-2 layer.

Complexity:

```text
O(V + E)
```

Every vertex is processed, and every adjacency-list edge is examined.

---

# 11. DFS

DFS means:

> **Depth-First Search**

Instead of spreading outward like BFS, DFS follows a path as deeply as possible before backing up.

Example:

```text
A
├── B
│   ├── D
│   └── E
└── C
```

A possible DFS order:

```text
A → B → D → E → C
```

## Why does DFS use a stack?

Because we want the **most recently discovered** vertex to be processed next.

That's LIFO.

DFS can therefore be implemented using:

```python
stack = [start]
```

or recursively using the call stack.

## Iterative DFS

```python
def dfs(graph, start):
    stack = [start]
    visited = set()
    order = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)

    return order
```

The exact traversal order can depend on the order neighbors are pushed.

Complexity:

```text
O(V + E)
```

---

# 12. Connected Components

A connected component is a group of vertices where every vertex is reachable from every other vertex within that group.

Example:

```text
A —— B —— C       D —— E       F
```

There are three components:

```text
{A, B, C}
{D, E}
{F}
```

## How do we find them?

Use BFS or DFS.

Start from an unvisited vertex.

Everything reached belongs to its component.

Then find another unvisited vertex and repeat.

```python
components = []

for vertex in graph:
    if vertex not in visited:
        component = bfs(vertex)
        components.append(component)
```

The important conceptual connection:

> **Connected components aren't a completely new traversal algorithm.**

They're an application of BFS/DFS.

---

# 13. Cycle Detection

A cycle exists when you can follow edges and eventually return to a vertex you've already encountered in the relevant traversal.

For an undirected graph, DFS can keep track of the parent:

```text
A
|
B
|
C
```

When C sees B, that's normal — B is its parent.

But if C encounters some already-visited vertex that **isn't its parent**, we've found a cycle.

Conceptually:

```text
if neighbor is visited and neighbor != parent:
    cycle exists
```

For directed graphs, the logic is different because direction matters.

---

# 14. Directed Graphs

An undirected edge:

```text
A —— B
```

means:

```text
A → B
B → A
```

A directed graph can instead have:

```text
A → B
```

without:

```text
B → A
```

Your adjacency representation therefore stores outgoing edges.

Example:

```python
graph = {
    "A": {"B"},
    "B": {"C"},
    "C": set()
}
```

This means:

```text
A → B → C
```

---

# 15. Weakly vs Strongly Connected

These sound terrifying but the distinction is simple.

## Weakly connected

Ignore edge directions.

```text
A → B → C
```

becomes:

```text
A —— B —— C
```

If the resulting undirected graph is connected, the directed graph is **weakly connected**.

## Strongly connected

Direction must work both ways through directed paths.

For example:

```text
A → B
↑   ↓
└── C
```

Every vertex can reach every other vertex.

That's strong connectivity.

The key distinction:

> **Weak = connectivity after ignoring direction.**

> **Strong = directed reachability between every pair.**

---

# 16. Weighted Graphs

Now edges carry values:

```text
A ——5—— B
|
2
|
C
```

The edge isn't merely "A connects to B."

It says:

```text
A → B costs 5
A → C costs 2
```

Your weighted adjacency list stores this naturally:

```python
graph = {
    "A": {"B": 5, "C": 2},
    "B": {"A": 5},
    "C": {"A": 2}
}
```

So:

```python
graph["A"]["B"]
```

gives:

```text
5
```

---

# 17. Dijkstra's Algorithm

## Problem

Find the shortest distance from one starting vertex to every other vertex in a weighted graph with **non-negative edge weights**.

Example:

```text
A --4-- B
|       |
1       2
|       |
C --1-- D
```

Starting from A:

```text
A = 0
C = 1
D = 2
B = 4
```

The key question is:

> Which vertex should we process next?

Dijkstra chooses the **currently closest unprocessed vertex**.

That is the greedy part.

---

## Step 1 — initialize distances

```python
distances = {
    vertex: float("inf")
    for vertex in graph
}
```

Initially, we know nothing.

```text
A = ∞
B = ∞
C = ∞
D = ∞
```

Then:

```python
distances[start] = 0
```

because the distance from the starting vertex to itself is zero.

---

## Step 2 — priority queue

```python
heap = [(0, start)]
```

The heap stores:

```text
(distance, vertex)
```

The smallest distance comes out first.

So instead of scanning every vertex repeatedly, we can efficiently ask:

> Who currently has the smallest known distance?

---

## Step 3 — take the closest vertex

```python
distance, current = heapq.heappop(heap)
```

Suppose:

```text
heap = [
    (2, C),
    (4, B),
    (7, D)
]
```

Then C comes out.

This means:

> The currently best candidate is C at distance 2.

---

## Step 4 — relax its edges

Suppose:

```text
C --3-- D
```

Then reaching C costs 2.

Going:

```text
A → C → D
```

costs:

```text
2 + 3 = 5
```

So:

```python
candidate = distance + weight
```

Then:

```python
if candidate < distances[neighbor]:
    distances[neighbor] = candidate
```

If we previously believed D was reachable in 7:

```text
5 < 7
```

so we improve our answer.

This operation is called **relaxation**.

### Relaxation means:

> "I found a way to reach this vertex that is cheaper than the best way I currently know."

That's it.

---

## Step 5 — record the path

Distances tell us:

```text
A → D = 5
```

But they don't tell us **how**.

So we maintain:

```python
previous = {
    vertex: None
    for vertex in graph
}
```

When we improve a neighbor:

```python
previous[neighbor] = current
```

If:

```text
A → C → D
```

was the shortest route, we get:

```text
previous[D] = C
previous[C] = A
previous[A] = None
```

Then we can reconstruct:

```text
D → C → A
```

and reverse it:

```text
A → C → D
```

---

## Complete Dijkstra

```python
import heapq

def dijkstra(graph, start):

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
```

### The entire algorithm in plain English

```text
1. Every distance starts at infinity.
2. The start vertex has distance 0.
3. Put the start into a min-heap.
4. Take the currently closest vertex.
5. Look at each edge leaving it.
6. Ask whether going through this vertex gives a shorter route.
7. If yes:
      update the distance
      remember the previous vertex
      put the new distance into the heap
8. Repeat.
```

### Why doesn't Dijkstra handle negative weights?

Because its greedy assumption depends on this:

> Once the closest vertex has been selected, a later path cannot make it cheaper.

With non-negative edges, that's safe.

With a negative edge, you could have:

```text
A → B = 5
```

and Dijkstra thinks:

```text
B = 5
```

is finalized.

But later:

```text
A → C = 10
C → B = -20
```

gives:

```text
A → C → B = -10
```

So B wasn't actually finalized.

That's why Dijkstra requires non-negative edge weights.

---

# 18. Dijkstra: Distance vs Path

These are two different pieces of information.

### `distances`

Answers:

> How expensive is the shortest route?

Example:

```python
distances["D"]
# 5
```

### `previous`

Answers:

> Which vertex did we come from on that shortest route?

Example:

```python
previous["D"]
# "C"
```

Then:

```python
def build_path(previous, destination):

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path
```

So:

```text
previous:
D → C
C → A
A → None
```

becomes:

```text
D → C → A
```

then:

```text
A → C → D
```

---

# 19. Greedy Algorithms

A **greedy algorithm** repeatedly makes what appears to be the best choice at the current moment.

It does not generally reconsider previous choices.

Dijkstra is greedy because it repeatedly chooses:

> the currently closest unprocessed vertex.

Important:

**Greedy is a strategy, not a data structure.**

Therefore an algorithm can belong to multiple categories.

Dijkstra is:

```text
Graph algorithm
+
Greedy algorithm
+
Shortest-path algorithm
```

---

# 20. The Big Picture

The important thing to remember is that these topics aren't isolated islands.

They build on each other.

```text
Data structures
│
├── Array
├── Linked List
├── Stack
├── Queue
└── Hash Table
       │
       ▼
    Graph representation
       │
       ├── BFS
       │    └── Connected Components
       │
       ├── DFS
       │    ├── Connected Components
       │    └── Cycle Detection
       │
       └── Weighted Graph
              │
              └── Dijkstra
                     └── Path Reconstruction
```

And several ideas cross-connect:

```text
Queue  → BFS
Stack  → DFS
Hash Set → visited
Heap   → efficient Dijkstra
Hash Map → distances / previous
```

That's the part I want you to eventually internalize.

You don't need to remember **50 independent algorithms**.

You need to remember a relatively small collection of ideas and understand how they combine.

---

# 21. What You Should Be Able to Recall

When you revisit this notebook later, try to answer these without looking:

### Data structures

- Why is array indexing O(1)?
- Why is inserting at the beginning O(n)?
- What makes a linked list different?
- Why is a stack LIFO?
- Why is a queue FIFO?
- Why are hash tables useful?

### Searching

- What does binary search require?
- Why is it O(log n)?
- Why is binary search different from a BST?

### Graphs

- What is an adjacency list?
- What is the difference between directed and undirected?
- What does BFS do?
- Why does BFS use a queue?
- Why does BFS give shortest paths in an unweighted graph?
- What does DFS do?
- Why does DFS use a stack?
- What is a connected component?
- What is a cycle?
- Weak vs strong connectivity?

### Weighted graphs

- What does an edge weight represent?
- What is Dijkstra trying to calculate?
- Why does it use a min-heap?
- What is relaxation?
- Why does `candidate = distance + weight` make sense?
- What does `previous` store?
- How do we reconstruct a path?
- Why can't Dijkstra safely handle negative weights?
- Why is Dijkstra considered greedy?

If you can answer those **without opening the notes**, the information is starting to move from temporary memory into something much more durable.

And this document should be treated as a **living revision notebook**, not something you read once and forget. When you properly learn/practice a topic, we can add the things that specifically confused you, your own implementation, mistakes you've made, and examples that made the concept click.