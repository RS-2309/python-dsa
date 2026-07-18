from max_heap import MaxHeap

print("========== MAX HEAP TEST ==========\n")

heap = MaxHeap()

print("Empty Heap:")
print(heap)
print("Length:", len(heap))
print("Peek:", heap.peek())
print()

print("Inserting elements...")

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    heap.insert(value)

print("Inserted:", values)
print("Heap:", heap)
print("Length:", len(heap))
print("Peek:", heap.peek())
print()

print("Deleting elements...")

while len(heap):
    print("Deleted:", heap.delete())
    print(heap)

print()

print("Delete from empty heap:")
print(heap.delete())
print()

print("Testing duplicates...")

duplicates = MaxHeap()

duplicates.insert(10)
duplicates.insert(10)
duplicates.insert(10)

print(duplicates)

while len(duplicates):
    print("Deleted:", duplicates.delete())

print()

print("Testing single element heap...")

single = MaxHeap()

single.insert(42)

print(single)
print("Peek:", single.peek())
print("Delete:", single.delete())
print(single)

print()

print("========== TEST COMPLETE ==========")