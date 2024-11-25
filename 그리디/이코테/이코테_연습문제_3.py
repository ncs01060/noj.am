n = int(input())
heros_scared = list(map(int,input().split()))
heros = 0
count = 0
for i in sorted(heros_scared):
    heros += i
    if heros == n:
        count+=1
        heros = 0
        

print(count)