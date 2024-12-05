from collections import deque
computer = int(input())
n = int(input())
computers = [[0] * (computer+1) for _ in range(computer+1)]
visited = [False] * (computer+1)
for i in range(n):
    f,k = map(int,input().split())
    computers[f][k] = computers[k][f] = 1

def bfs(metrix,v,visited):
    queue = deque()
    queue.append(v)
    cnt = 0
    while queue:
        value = queue.popleft()
        if not visited[value]:
            cnt+=1
            visited[value] = True
        for c in range(len(metrix[value])):
            if metrix[value][c] == 1 and not visited[c]:
                queue.append(c)
    print(cnt-1)
    
bfs(computers,1,visited)