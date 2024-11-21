import sys;input = sys.stdin.readline
n,m = map(int,input().split())

num_poki = {}
name_poki = {}

for i in range(1,n+1):
    poki = input().strip()
    num_poki[i] = poki
    name_poki[poki] = i

for _ in range(m):
    qes = input().strip()
    if qes.isdigit():
        print(num_poki[int(qes)])
    else:
        print(name_poki[qes])