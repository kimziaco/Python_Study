from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

queue.popleft() #왼쪽에 있는 원소를 제거
queue.popleft()

print(queue)
queue.reverse()
print(queue)
