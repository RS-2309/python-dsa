from hash_table import HashTable

print("========== HASH TABLE TEST ==========\n")

# Constructor
table = HashTable()

print("Empty table:")
print(table)
print(f"Length: {len(table)}")
print()

# Insert
print("Adding elements...")
table["cat"] = 7
table["dog"] = 10
table["goat"] = 15
table["cow"] = 20

print(table)
print(f"Length: {len(table)}")
print()

# Get item
print("Accessing values:")
print("cat =", table["cat"])
print("dog =", table["dog"])
print()

# Update existing key
print("Updating 'cat'...")
table["cat"] = 100
print("cat =", table["cat"])
print(table)
print()

# Contains
print("'cat' in table:", "cat" in table)
print("'lion' in table:", "lion" in table)
print()

# Resize Up
print("Adding many items (resize up)...")
for i in range(20):
    table[f"key{i}"] = i

print(table)
print(f"Length: {len(table)}")
print(f"Number of buckets: {len(table.buckets)}")
print()

# Delete
print("Deleting...")
del table["dog"]
del table["cow"]

print(table)
print(f"Length: {len(table)}")
print()

# Resize Down
print("Deleting extra keys (resize down)...")
for i in range(20):
    del table[f"key{i}"]

print(table)
print(f"Length: {len(table)}")
print(f"Number of buckets: {len(table.buckets)}")
print()

# Exception tests
print("Testing exceptions:")

try:
    print(table["dog"])
except KeyError as e:
    print(f"KeyError: {e}")

try:
    del table["lion"]
except KeyError as e:
    print(f"KeyError: {e}")

print()

# Constructor validation
print("Constructor validation:")

tests = [0, -4, 3, "hello"]

for value in tests:
    try:
        HashTable(value)
    except Exception as e:
        print(f"HashTable({value!r}) -> {type(e).__name__}: {e}")

print("\n========== TEST COMPLETE ==========")