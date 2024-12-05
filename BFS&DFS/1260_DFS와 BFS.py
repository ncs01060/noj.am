from collections import deque
n,m,v = map(int,input().split())
metrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    t,f = map(int,input().split())
    metrix[t][f] = metrix[f][t] = 1

# 깊이 우선 탐색(Stack)
def dfs(metrix,visited,v):
    stack = [v]
    while stack:
        value = stack.pop()
        if not visited[value]:
            print(value,end=' ')
            visited[value] = True
        for c in range(len(metrix)-1,-1,-1):
            if metrix[value][c] == 1 and not visited[c]:
                stack.append(c)
        
dfs(metrix,visited,v)
print()

# 넓이 우선 탐색 (Queue)
def bfs(metrix,v,visited):
    queue = deque()
    queue.append(v)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            print(value,end=' ')
            visited[value] = True
        for c in range(len(metrix[value])):
            if metrix[value][c] == 1 and not visited[c]:
                queue.append(c)

visited = [False] * (n+1)
bfs(metrix,v,visited)


