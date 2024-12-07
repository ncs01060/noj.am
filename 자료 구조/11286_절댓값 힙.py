from collections import deque
import sys; input = sys.stdin.readline
n = int(input())
queue = deque()

for i in range(n):
    s = int(input())
    if s == 0: 
        if not queue:
            print(0)
        else:
            new_queue = deque()
            for j in queue:
                new_queue.append(abs(j))
            ls = abs(min(new_queue))
            if -1 * ls in queue:
                print(-1 * ls)
                queue.remove(-1 * ls)
            else:
                print(ls)
                queue.remove(ls)
    else:
        queue.append(s)


