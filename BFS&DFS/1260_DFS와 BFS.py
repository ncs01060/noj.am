def dfs(V):
    print(g)
    visited[V] = True  # 해당 V값 방문처리
    print(V, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and g[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

n,m,v = map(int,input().split())
g = [[0] * (n+1) for _ in range(n + 1)]
for i in range(m):
    x,y=map(int,input().split())
    g[x][y] = g[y][x] = 1


visited = [False] * (len(g)+1)
dfs(v)
