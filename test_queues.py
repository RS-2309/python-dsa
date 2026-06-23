from Queues import Queue
q = Queue()

q.enqueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q)

print(10 in q)
print(15 in q)

print(len(q))

print(q.is_empty())

print(q.peek())

print(q.dequeue())

print(len(q))

print(q)

q.clear()

print(len(q))

print(q)