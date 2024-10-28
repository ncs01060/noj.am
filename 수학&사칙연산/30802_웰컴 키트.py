n=int(input())
size = list(map(int,input().split()))
t,p = map(int,input().split())

t_count = 0
p_count = 0

p_count = n//p

for i in size:
    if i % t == 0:
        t_count += i//t
    else:
        t_count += i//t+1

print("%d\n%d %d"%(t_count,p_count,n%p))
