# Hash Tables

A hash table implementation written from scratch in Python using **separate chaining** for collision handling and **dynamic resizing** based on the current load factor.

This implementation was created as part of my DSA learning journey to understand how Python dictionaries work internally and how hash tables achieve near constant-time operations.

---

## Files

```text
hash_table.py
test_hash_table.py
```

* **hash_table.py** – Contains the `HashTable` class.
* **test_hash_table.py** – Contains test cases for the implementation.

---

## Features

### Implemented

* Insert key-value pairs
* Retrieve values by key
* Update existing keys
* Delete key-value pairs
* Membership testing using `in`
* Length using `len()`
* Automatic resizing
* Automatic shrinking
* String representation for easy visualization

---

## Collision Resolution

This implementation uses **Separate Chaining**.

Each bucket stores a list of `(key, value)` tuples.

When multiple keys hash to the same bucket, they are stored together within that bucket.

---

## Dynamic Resizing

The table automatically adjusts its capacity based on the current load factor.

### Expand

The table doubles in size whenever:

```text
Load Factor > 0.75
```

### Shrink

The table halves its size whenever:

```text
Load Factor < 0.375
```

The table never shrinks below its original capacity.

---

## Supported Operations

| Method               | Description                               |
| -------------------- | ----------------------------------------- |
| `table[key] = value` | Insert or update a key-value pair.        |
| `table[key]`         | Retrieve the value associated with a key. |
| `del table[key]`     | Remove a key-value pair.                  |
| `key in table`       | Check whether a key exists.               |
| `len(table)`         | Return the number of stored elements.     |

---

## Python Special Methods

| Method         | Purpose                                       |
| -------------- | --------------------------------------------- |
| `__repr__`     | Displays the hash table in a readable format. |
| `__setitem__`  | Enables dictionary-style insertion.           |
| `__getitem__`  | Enables dictionary-style lookup.              |
| `__delitem__`  | Enables dictionary-style deletion.            |
| `__contains__` | Enables the `in` keyword.                     |
| `__len__`      | Enables the use of `len()`.                   |

Example:

```python
table = HashTable()

table["apple"] = 10
table["banana"] = 20

print(table["apple"])
# 10

print("banana" in table)
# True

del table["apple"]

print(len(table))
# 1
```

---

## Time Complexity

| Operation | Average | Worst |
| --------- | :-----: | :---: |
| Insert    |   O(1)  |  O(n) |
| Search    |   O(1)  |  O(n) |
| Delete    |   O(1)  |  O(n) |
| Resize    |    —    |  O(n) |

---

## Design Choices

* Uses **separate chaining** for collision handling.
* Buckets are implemented as Python lists.
* Automatically expands and shrinks based on the load factor.
* Prevents shrinking below the initial table size.
* Supports Python's dictionary-like syntax through special methods.

---

## Future Improvements

* Implement iterators (`keys()`, `values()`, `items()`)
* Support custom hash functions
* Implement open addressing for comparison
* Improve string formatting for large tables
* Add comprehensive edge-case tests

---

## Learning Objective

This implementation was created to understand:

* Hash functions
* Collision handling
* Separate chaining
* Load factor
* Dynamic resizing
* Amortized time complexity
* Python special methods