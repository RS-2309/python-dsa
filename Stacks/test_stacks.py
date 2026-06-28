from stack import Stack

print("========== STACK TEST ==========\n")

# Constructor
stack = Stack()

print("Empty stack:")
print(stack)
print(f"Length: {len(stack)}")
print(f"Is Empty: {stack.is_empty()}")
print()

# Push
print("Adding elements...")
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print(stack)
print(f"Length: {len(stack)}")
print(f"Top: {stack.peek()}")
print()

# Contains
print("Membership testing...")
print("20 in stack:", 20 in stack)
print("100 in stack:", 100 in stack)
print()

# Pop
print("Removing elements...")

print("Popped:", stack.pop())
print(stack)

print("Popped:", stack.pop())
print(stack)

print(f"Length: {len(stack)}")
print(f"Top: {stack.peek()}")
print()

# Push Again
print("Adding more elements...")
stack.push(50)
stack.push(60)

print(stack)
print(f"Length: {len(stack)}")
print(f"Top: {stack.peek()}")
print()

# Clear
print("Clearing stack...")
stack.clear()

print(stack)
print(f"Length: {len(stack)}")
print(f"Is Empty: {stack.is_empty()}")
print()

# Exception Tests
print("Testing exceptions...")

try:
    stack.pop()
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    stack.peek()
except Exception as e:
    print(f"{type(e).__name__}: {e}")

print()

# Edge Cases
print("Testing edge cases...")

single = Stack()

single.push(99)

print(single)
print("Peek:", single.peek())
print("Popped:", single.pop())
print(single)

print()

print("========== TEST COMPLETE ==========")