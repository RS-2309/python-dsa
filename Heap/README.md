# Heaps

A Min Heap and Max Heap implementation written from scratch in Python using arrays.

This implementation was created as part of my Data Structures & Algorithms (DSA) learning journey to understand how heaps maintain ordering properties while supporting efficient insertion and deletion.

---

## Files

```text
min_heap.py
max_heap.py
test_min_heap.py
test_max_heap.py
```

- **min_heap.py** – Contains the `MinHeap` implementation.
- **max_heap.py** – Contains the `MaxHeap` implementation.
- **test_min_heap.py** – Demonstrates and tests all `MinHeap` operations.
- **test_max_heap.py** – Demonstrates and tests all `MaxHeap` operations.

---

## Features

### Min Heap

- Insert values
- Delete the minimum value
- Peek at the minimum value
- Length support using `len()`
- String representation using `repr()`

### Max Heap

- Insert values
- Delete the maximum value
- Peek at the maximum value
- Length support using `len()`
- String representation using `repr()`

---

## Supported Operations

| Method | Description |
|--------|-------------|
| `insert(value)` | Inserts a value while maintaining heap properties. |
| `delete()` | Removes and returns the root node. |
| `peek()` | Returns the root node without removing it. |

---

## Python Special Methods

| Method | Purpose |
|--------|--------|
| `__repr__` | Displays the underlying array representation. |
| `__len__` | Enables the use of `len()`. |

---

## Examples

### Min Heap

```python
heap = MinHeap()

heap.insert(50)
heap.insert(30)
heap.insert(20)

print(heap)
# [20, 50, 30]

print(heap.peek())
# 20

print(heap.delete())
# 20
```

### Max Heap

```python
heap = MaxHeap()

heap.insert(50)
heap.insert(30)
heap.insert(70)

print(heap)
# [70, 30, 50]

print(heap.peek())
# 70

print(heap.delete())
# 70
```

---

## Heap Properties

### Min Heap

Every parent node is less than or equal to its children.

```text
      20
     /  \
   30    40
  / \
50  60
```

### Max Heap

Every parent node is greater than or equal to its children.

```text
      80
     /  \
   60    70
  / \
20  40
```

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Insert | O(log n) |
| Delete | O(log n) |
| Peek | O(1) |
| Length | O(1) |
| Representation | O(n) |

---

## Design Choices

- Implemented using Python lists.
- Uses recursive heapify operations.
- Supports both Min Heap and Max Heap.
- Duplicate values are supported.
- Root node is always stored at index `0`.

---

## Learning Objectives

This implementation was created to understand:

- Complete Binary Trees
- Heap Properties
- Array-Based Tree Representation
- Heapify Up
- Heapify Down
- Priority Queues
- Logarithmic Operations