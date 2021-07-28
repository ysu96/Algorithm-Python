from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.popleft()
queue.append(5)
print(queue)
queue.reverse()
print(queue)
