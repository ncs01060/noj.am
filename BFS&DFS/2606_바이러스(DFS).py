computer = int(input())
n = int(input())
computers = [[0] * (computer+1) for _ in range(computer+1)]
visited = [False] * (computer+1)
for i in range(n):
    f,k = map(int,input().split())
    computers[f][k] = computers[k][f] = 1

def dfs(metrix,v,visited):
    stack = [v]
    cnt = 0
    while stack:
        value = stack.pop()
        if not visited[value]:
            cnt+=1
            visited[value] = True
        for c in range(len(metrix)):
            if metrix[value][c] == 1 and not visited[c]:
                stack.append(c)
    print(cnt-1)
    


dfs(computers,1,visited)
