from Linked_Lists import LinkedList
l = LinkedList()

l.append(10)
l.append(20)
l.append(30)
l.prepend(5)

print(l)

l.insert(40, 2)

print(l)

l.delete(5)

print(l)

l.reverse()

print(l)

print(20 in l)
print(25 in l)

print(len(l))

print(l.pop())

print(l)

print(l.get(1))