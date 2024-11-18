n=int(input())
border = [list(map(int,input().split())) for _ in range(n)]
for i in sorted(border,key=lambda x:(x[1],x[0])):
    print(*i)