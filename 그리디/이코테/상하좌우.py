n = int(input())
x,y = 1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
types = ['L','R','U','D']
cmd = list(map(str,input().split()))
for plan in cmd:
    for i in range(len(types)):
        if plan == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny

        
print(x,y)