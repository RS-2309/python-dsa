# Queues

A queue implementation written from scratch in Python using a singly linked list.

This implementation follows the **FIFO (First In, First Out)** principle, where the first element inserted is the first one to be removed.

---

## Files

```text
queue.py
test_queue.py
```

* **queue.py** – Contains the `QueueNode` and `Queue` classes.
* **test_queue.py** – Contains test cases for the queue implementation.

---

## Features

### Implemented

* Enqueue elements
* Dequeue elements
* Peek at the front element
* Check if the queue is empty
* Clear the queue
* Membership testing using `in`
* Length using `len()`
* Readable string representation

---

## Supported Operations

| Method           | Description                                       |
| ---------------- | ------------------------------------------------- |
| `enqueue(value)` | Adds an element to the rear of the queue.         |
| `dequeue()`      | Removes and returns the front element.            |
| `peek()`         | Returns the front element without removing it.    |
| `is_empty()`     | Returns `True` if the queue contains no elements. |
| `clear()`        | Removes all elements from the queue.              |

---

## Python Special Methods

| Method         | Purpose                                  |
| -------------- | ---------------------------------------- |
| `__repr__`     | Displays the queue in a readable format. |
| `__contains__` | Enables the use of the `in` keyword.     |
| `__len__`      | Enables the use of `len()`.              |

Example:

```python
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue)
# [10, 20, 30]

print(queue.peek())
# 10

print(queue.dequeue())
# 10

print(len(queue))
# 2

print(20 in queue)
# True
```

---

## Time Complexity

| Operation             | Time Complexity |
| --------------------- | --------------- |
| Enqueue               | O(1)            |
| Dequeue               | O(1)            |
| Peek                  | O(1)            |
| Is Empty              | O(1)            |
| Clear                 | O(1)            |
| Length (`len`)        | O(1)            |
| Search (`in`)         | O(n)            |
| String Representation | O(n)            |

---

## Design Choices

* Implemented using a singly linked list.
* Maintains both a **head** (front) and **tail** (rear) pointer.
* A `size` attribute is maintained, allowing `len(queue)` to execute in **O(1)** time.
* `enqueue()` inserts at the tail and `dequeue()` removes from the head, ensuring constant-time performance.

---

## Learning Objective

This implementation was created to understand:

* Queue data structure
* FIFO behavior
* Linked-list-based implementation
* Constant-time insertion and deletion
* Time complexity analysis
* Python object-oriented programming