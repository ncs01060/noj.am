n=int(input())
sw = False
for i in range(n):
    cnt = 0
    for j in str(i):
        cnt+=int(j)
    if cnt+i == n:
        sw = True
        cnt = i
        break

if sw:
    print(cnt)
else:
    print(0)