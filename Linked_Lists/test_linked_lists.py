from linked_list import LinkedList

print("========== LINKED LIST TEST ==========\n")

# Constructor
linked_list = LinkedList()

print("Empty linked list:")
print(linked_list)
print(f"Length: {len(linked_list)}")
print()

# Append
print("Appending elements...")
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print(linked_list)
print(f"Length: {len(linked_list)}")
print()

# Prepend
print("Prepending element...")
linked_list.prepend(5)

print(linked_list)
print()

# Insert
print("Inserting elements...")
linked_list.insert(15, 2)
linked_list.insert(100, 0)
linked_list.insert(999, len(linked_list))

print(linked_list)
print()

# Get
print("Getting elements...")
print("Index 0:", linked_list.get(0))
print("Index 3:", linked_list.get(3))
print("Last Index:", linked_list.get(len(linked_list) - 1))
print()

# Contains
print("Membership testing...")
print("20 in linked list:", 20 in linked_list)
print("500 in linked list:", 500 in linked_list)
print()

# Delete
print("Deleting elements...")
linked_list.delete(15)
linked_list.delete(100)
linked_list.delete(999)

print(linked_list)
print(f"Length: {len(linked_list)}")
print()

# Pop
print("Popping elements...")

print("Pop last:", linked_list.pop())
print(linked_list)

print("Pop first:", linked_list.pop(0))
print(linked_list)

print("Pop index 2:", linked_list.pop(2))
print(linked_list)
print()

# Reverse
print("Reversing linked list...")
linked_list.reverse()

print(linked_list)
print()

# Exception Tests
print("Testing exceptions...")

try:
    linked_list.get(100)
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    linked_list.insert(1, 100)
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    linked_list.delete(99999)
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    empty = LinkedList()
    empty.pop()
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    empty.delete(10)
except Exception as e:
    print(f"{type(e).__name__}: {e}")

print()

# Edge Cases
print("Testing edge cases...")

single = LinkedList()
single.append(42)

print("Single element:")
print(single)

single.reverse()
print("After reverse:")
print(single)

single.pop()
print("After pop:")
print(single)

print()

print("========== TEST COMPLETE ==========")