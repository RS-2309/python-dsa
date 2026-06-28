# Stacks

A stack implementation written from scratch in Python using a singly linked list.

This implementation follows the **LIFO (Last In, First Out)** principle, where the last element inserted is the first one to be removed.

---

## Files

```text
stack.py
test_stack.py
```

* **stack.py** – Contains the `StackNode` and `Stack` classes.
* **test_stack.py** – Contains test cases for the stack implementation.

---

## Features

### Implemented

* Push elements onto the stack
* Pop elements from the stack
* Peek at the top element
* Check if the stack is empty
* Clear the stack
* Membership testing using `in`
* Length using `len()`
* Readable string representation

---

## Supported Operations

| Method        | Description                                       |
| ------------- | ------------------------------------------------- |
| `push(value)` | Adds an element to the top of the stack.          |
| `pop()`       | Removes and returns the top element.              |
| `peek()`      | Returns the top element without removing it.      |
| `is_empty()`  | Returns `True` if the stack contains no elements. |
| `clear()`     | Removes all elements from the stack.              |

---

## Python Special Methods

| Method         | Purpose                                  |
| -------------- | ---------------------------------------- |
| `__repr__`     | Displays the stack in a readable format. |
| `__contains__` | Enables the use of the `in` keyword.     |
| `__len__`      | Enables the use of `len()`.              |

Example:

```python
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack)
# [30, 20, 10]

print(stack.peek())
# 30

print(stack.pop())
# 30

print(len(stack))
# 2

print(20 in stack)
# True
```

---

## Time Complexity

| Operation             | Time Complexity |
| --------------------- | --------------- |
| Push                  | O(1)            |
| Pop                   | O(1)            |
| Peek                  | O(1)            |
| Is Empty              | O(1)            |
| Clear                 | O(1)            |
| Length (`len`)        | O(1)            |
| Search (`in`)         | O(n)            |
| String Representation | O(n)            |

---

## Design Choices

* Implemented using a singly linked list.
* The top of the stack is stored at the head of the list.
* A `size` attribute is maintained, allowing `len(stack)` to execute in **O(1)** time.
* Push and pop operations both occur at the head, making them constant-time operations.

---

## Future Improvements

* Add an iterator (`__iter__`)
* Support copying and deep copying
* Add optional type hints
* Expand test coverage with additional edge cases

---

## Learning Objective

This implementation was created to understand:

* Stack data structure
* LIFO behavior
* Linked-list-based implementation
* Constant-time insertion and deletion
* Time complexity analysis
* Python object-oriented programming