n,m = map(int,input().split())
metrix = [[0] * (m+1) for _ in range(m+1)]
visited = [False] * (m+1)
for i in range(m):
    k,f = map(int,input().split())
    metrix[k][f] = metrix[f][k] = 1


def dfs(metrix,v,visited):
    
    result = 0
    for i in range(1,v+1):
        stack = [i]
        cnt = 0
        while stack:
            value = stack.pop()
            if not visited[value]:
                cnt+=1
                visited[value] = True
            for c in range(len(metrix)):
                if metrix[value][c] == 1 and not visited[c]:
                    stack.append(c)
        result = max(result,cnt)
    
    print(result-1)


dfs(metrix,m,visited)

    