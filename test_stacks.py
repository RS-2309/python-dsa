from Stacks import Stack
s = Stack()

s.push(5)
s.push(10)
s.push(20)
s.push(30)

print(s)

print(10 in s)
print(15 in s)

print(len(s))

print(s.is_empty())

print(s.peek())

print(s.pop())

print(len(s))

print(s)

s.clear()

print(len(s))

print(s)