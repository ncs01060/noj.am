n = int(input())
days = list(map(int,input().split()))
burn = 0
result = 0
for i in days:
    if i == 1:
        burn+=1
        result+=burn
    else:
        burn-=1
        result+=burn

print(result)