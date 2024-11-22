n = int(input())
l = [int(input()) for _ in range(n)]

if sum(l) == 0:
    print(0)
else:
    EPS = 1e-9
    lf = round(len(l)*0.15 + EPS)
    l = sorted(l)
    result = 0
    cnt=0

    for i in range(lf,len(l)-lf):
        cnt+=1
        result += l[i]

    print(round(result/cnt+EPS))
