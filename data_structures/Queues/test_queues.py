from queue import Queue

print("========== QUEUE TEST ==========\n")

# Constructor
queue = Queue()

print("Empty queue:")
print(queue)
print(f"Length: {len(queue)}")
print(f"Is Empty: {queue.is_empty()}")
print()

# Enqueue
print("Adding elements...")
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print(queue)
print(f"Length: {len(queue)}")
print(f"Front: {queue.peek()}")
print()

# Contains
print("Membership testing...")
print("20 in queue:", 20 in queue)
print("100 in queue:", 100 in queue)
print()

# Dequeue
print("Removing elements...")

print("Dequeued:", queue.dequeue())
print(queue)

print("Dequeued:", queue.dequeue())
print(queue)

print(f"Length: {len(queue)}")
print(f"Front: {queue.peek()}")
print()

# Enqueue Again
print("Adding more elements...")
queue.enqueue(50)
queue.enqueue(60)

print(queue)
print(f"Length: {len(queue)}")
print()

# Clear
print("Clearing queue...")
queue.clear()

print(queue)
print(f"Length: {len(queue)}")
print(f"Is Empty: {queue.is_empty()}")
print()

# Exception Tests
print("Testing exceptions...")

try:
    queue.dequeue()
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    queue.peek()
except Exception as e:
    print(f"{type(e).__name__}: {e}")

print()

# Edge Cases
print("Testing edge cases...")

single = Queue()

single.enqueue(99)

print(single)
print("Peek:", single.peek())
print("Dequeued:", single.dequeue())
print(single)

print()

print("========== TEST COMPLETE ==========")