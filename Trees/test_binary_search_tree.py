from binary_search_tree import BinarySearchTree

print("========== BINARY SEARCH TREE TEST ==========\n")

# Constructor
tree = BinarySearchTree()

print("Empty tree created.")
print("Node Count:", tree.count_nodes())
print("Height:", tree.height())
print("Minimum:", tree.minimum())
print("Maximum:", tree.maximum())
print("Length:", len(tree))
print("Is Empty:", tree.is_empty())
print()

# Insert
print("Inserting elements...")

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.insert(value)

print("Inserted:", values)
print()

# Search
print("Searching...")
print("40 in tree:", 40 in tree)
print("100 in tree:", 100 in tree)
print()

# Length
print("Length")
print(len(tree))
print()

# Node Count
print("Node Count")
print(tree.count_nodes())
print()

# Height
print("Height")
print(tree.height())
print()

# Leaf Count
print("Leaf Count")
print(tree.count_leaves())
print()

# Minimum & Maximum
print("Minimum:", tree.minimum())
print("Maximum:", tree.maximum())
print()

# String Representations
print("String Representation")
print(tree)
print()

print("Developer Representation")
print(repr(tree))
print()

# Traversals
print("Inorder Traversal")
print(tree.inorder())
print()

print("Preorder Traversal")
print(tree.preorder())
print()

print("Postorder Traversal")
print(tree.postorder())
print()

# Duplicate Insertions
print("Testing duplicate insertions...")

tree.insert(50)
tree.insert(50)
tree.insert(50)

print(tree.inorder())
print("Node Count:", tree.count_nodes())
print()

# Delete Leaf
print("Deleting leaf node (20)...")
tree.delete(20)

print(tree.inorder())
print()

# Delete Node with One Child
print("Deleting node with one child (30)...")
tree.delete(30)

print(tree.inorder())
print()

# Delete Node with Two Children
print("Deleting node with two children (70)...")
tree.delete(70)

print(tree.inorder())
print()

# Tree Statistics After Deletion
print("Tree Statistics")
print("Node Count:", tree.count_nodes())
print("Height:", tree.height())
print("Leaf Count:", tree.count_leaves())
print("Minimum:", tree.minimum())
print("Maximum:", tree.maximum())
print()

# Exception Tests
print("Testing exceptions...")

try:
    tree.delete(999)
except KeyError as e:
    print(f"KeyError: {e}")

print()

# Clear
print("Clearing tree...")
tree.clear()

print("Length:", len(tree))
print("Is Empty:", tree.is_empty())
print("Inorder:", tree.inorder())
print()

# Edge Cases
print("Testing edge cases...")

single = BinarySearchTree()

single.insert(10)

print("Single Node Tree")
print("Nodes:", single.count_nodes())
print("Height:", single.height())
print("Leaves:", single.count_leaves())
print("Inorder:", single.inorder())

single.delete(10)

print("\nAfter deleting the only node:")
print("Nodes:", single.count_nodes())
print("Height:", single.height())
print("Leaves:", single.count_leaves())
print("Minimum:", single.minimum())
print("Maximum:", single.maximum())
print()

print("========== TEST COMPLETE ==========")