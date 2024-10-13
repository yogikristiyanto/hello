from collections import deque
def enqueue(queue, item):
 queue.append(item)
def dequeue(queue):
 if len(queue) > 0:
  return queue.popleft()
 return None
queue = deque()
enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)
print("Dequeue:", dequeue(queue)) # Output: 1
print("Dequeue:", dequeue(queue)) # Output: 2
