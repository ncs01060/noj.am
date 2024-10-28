from collections import deque
a=int(input())

queue = deque(_ for _ in range(1,a+1))

while len(queue) != 1:
    queue.popleft()
    k = queue.popleft()
    queue.append(k)

print(*queue)