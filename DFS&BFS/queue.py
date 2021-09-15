from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

v = queue.popleft() #왼쪽에 있는 원소를 제거
print(v)

v = queue.popleft()
print(v)

print(queue)
queue.reverse()
print(queue)
