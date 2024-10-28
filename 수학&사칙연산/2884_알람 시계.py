t,m=map(int,input().split())
if m < 45:
    t-=1
    if t == -1:
        t = 23
    m+=15
else:
    m-=45

print(t,m)