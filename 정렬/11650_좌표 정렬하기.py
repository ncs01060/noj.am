n=int(input())
border = [list(map(int,input().split())) for _ in range(n)]
for i in sorted(border,key=lambda x:(x[0],x[1])):
    print(*i)