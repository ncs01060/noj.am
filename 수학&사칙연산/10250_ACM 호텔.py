a=int(input())

for i in range(a):
    H,W,P = map(int,input().split())
    h = 1
    w = 1
    for j in range(0,P):
        if h > H:
            w+=1
            h = 1
        h+=1
    print("%d%02d"%(h-1,w))
