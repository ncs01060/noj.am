n,m = map(int,input().split())
key = {}
for i in range(n):
    k,v = input().split()
    key[k] = v

for j in range(m):
    site = input()
    print(key[site])