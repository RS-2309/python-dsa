from Stacks import Stack
l = Stack()

l.push(5)
l.push(10)
l.push(20)
l.push(30)

print(l)

print(10 in l)
print(15 in l)

print(len(l))

print(l.is_empty())

print(l.peek())

print(l.pop())

print(len(l))

print(l)

l.clear()

print(len(l))

print(l)