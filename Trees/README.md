# Binary Search Tree

A Binary Search Tree (BST) implementation written from scratch in Python using recursion.

This implementation was created as part of my Data Structures & Algorithms (DSA) learning journey to understand how binary search trees organize data efficiently and support fast searching, insertion, and deletion.

---

## Files

```text
binary_search_tree.py
test_binary_search_tree.py
```

- **binary_search_tree.py** – Contains the `TreeNode` and `BinarySearchTree` classes.
- **test_binary_search_tree.py** – Demonstrates and tests all implemented operations.

---

## Features

### Implemented

- Insert values
- Search for values
- Delete nodes
- Count total nodes
- Count leaf nodes
- Calculate tree height
- Find minimum value
- Find maximum value
- Inorder traversal
- Preorder traversal
- Postorder traversal
- Membership testing using `in`
- Length support using `len()`
- String representation using `str()`
- Developer representation using `repr()`
- Empty-tree checking
- Tree clearing

---

## Supported Operations

| Method | Description |
|----------|-------------|
| `insert(value)` | Inserts a value while maintaining BST properties. |
| `search(value)` | Returns `True` if the value exists in the tree. |
| `delete(value)` | Deletes a node from the tree. |
| `count_nodes()` | Returns the total number of nodes. |
| `count_leaves()` | Returns the number of leaf nodes. |
| `height()` | Returns the height of the tree. |
| `minimum()` | Returns the smallest value. |
| `maximum()` | Returns the largest value. |
| `inorder()` | Returns the inorder traversal. |
| `preorder()` | Returns the preorder traversal. |
| `postorder()` | Returns the postorder traversal. |
| `is_empty()` | Returns whether the tree is empty. |
| `clear()` | Removes all nodes from the tree. |

---

## Python Special Methods

| Method | Purpose |
|----------|----------|
| `__contains__` | Enables the use of the `in` keyword. |
| `__len__` | Enables the use of `len()`. |
| `__repr__` | Developer-friendly representation. |
| `__str__` | Human-readable tree summary. |

---

## Example

```python
tree = BinarySearchTree()

tree.insert(50)
tree.insert(30)
tree.insert(70)

print(tree)

print(30 in tree)

print(len(tree))

print(tree.inorder())
```

Output:

```text
BinarySearchTree with root value: 50, Height: 2, Nodes: 3, Leaves: 2 Inorder: [30, 50, 70]

True

3

[30, 50, 70]
```

---

## Tree Traversals

### Inorder (Left → Root → Right)

Produces the values in sorted order for a Binary Search Tree.

### Preorder (Root → Left → Right)

Useful for copying or serializing a tree.

### Postorder (Left → Right → Root)

Useful for deleting an entire tree or evaluating expression trees.

---

## Time Complexity

| Operation | Average | Worst |
|------------|:-------:|:-----:|
| Insert | O(log n) | O(n) |
| Search | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Minimum | O(log n) | O(n) |
| Maximum | O(log n) | O(n) |
| Count Nodes | O(n) | O(n) |
| Count Leaves | O(n) | O(n) |
| Height | O(n) | O(n) |
| Traversals | O(n) | O(n) |
| Clear | O(1) | O(1) |
| Is Empty | O(1) | O(1) |

---

## Design Choices

- Implemented recursively for simplicity and readability.
- Duplicate values are ignored to preserve unique keys.
- Deletion supports:
  - Leaf nodes
  - Nodes with one child
  - Nodes with two children using the inorder successor
- Traversals return Python lists for easy testing and inspection.
- Length is computed through recursive node counting.

---

## Future Improvements

- Level-order traversal (BFS)
- Tree iterator (`__iter__`)
- AVL Tree
- Red-Black Tree
- Pretty tree visualization
- Lowest Common Ancestor
- Successor and predecessor operations

---

## Learning Objectives

This implementation was created to understand:

- Binary Search Tree properties
- Recursive tree algorithms
- Tree traversals
- Recursive insertion and deletion
- Inorder successors
- Tree height and leaf counting
- Average vs worst-case complexity
- Recursive problem decomposition