from collections import deque
n,m = map(int,input().split())
metrix = []


for i in range(n):
    metrix.append(list(map(int,input())))

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif metrix[nx][ny] == 0:
                continue
            if metrix[nx][ny] == 1:
                metrix[nx][ny] = metrix[x][y]+1
                queue.append((nx,ny))
    return metrix[n-1][m-1]

print(bfs(0,0))