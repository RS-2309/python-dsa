# Linked Lists

A singly linked list implementation written from scratch in Python.

This implementation was created as part of my DSA learning journey to understand how linked lists work internally without relying on Python's built-in list.

---

## Files

```text
linked_list.py
test_linked_list.py
```

* **linked_list.py** – Contains the `ListNode` and `LinkedList` classes.
* **test_linked_list.py** – Contains test cases for verifying the implementation.

---

## Features

### Implemented

* Create an empty linked list
* Append elements
* Prepend elements
* Insert at any valid index
* Delete by value
* Pop by index (supports `-1` for the last element)
* Reverse the linked list in-place
* Get an element by index
* Membership testing using `in`
* Length using `len()`
* String representation for easy printing

---

## Supported Operations

| Method                 | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `append(value)`        | Adds an element to the end of the list.          |
| `prepend(value)`       | Inserts an element at the beginning of the list. |
| `insert(value, index)` | Inserts an element at the specified index.       |
| `delete(value)`        | Removes the first occurrence of a value.         |
| `pop(index=-1)`        | Removes and returns an element by index.         |
| `reverse()`            | Reverses the linked list in-place.               |
| `get(index)`           | Returns the value stored at an index.            |

---

## Python Special Methods

This implementation also supports several Python dunder methods.

| Method         | Purpose                                        |
| -------------- | ---------------------------------------------- |
| `__repr__`     | Displays the linked list in a readable format. |
| `__contains__` | Enables the use of the `in` keyword.           |
| `__len__`      | Enables the use of `len()`.                    |

Example:

```python
ll = LinkedList()

ll.append(10)
ll.append(20)

print(ll)
# [10, 20]

print(len(ll))
# 2

print(20 in ll)
# True
```

---

## Time Complexity

| Operation      | Time Complexity |
| -------------- | --------------- |
| Append         | O(n)            |
| Prepend        | O(1)            |
| Insert         | O(n)            |
| Delete         | O(n)            |
| Pop            | O(n)            |
| Get            | O(n)            |
| Reverse        | O(n)            |
| Search (`in`)  | O(n)            |
| Length (`len`) | O(n)            |

---

## Future Improvements

* Implement an iterator (`__iter__`)
* Support negative indices for `get()`
* Optimize `append()` to O(1) using a tail pointer
* Add more edge-case tests
* Implement a doubly linked list

---

## Learning Objective

The purpose of this implementation is to understand:

* Nodes and pointers
* Dynamic memory-based data structures
* Traversal
* Insertion and deletion operations
* Time complexity analysis
* Python class design