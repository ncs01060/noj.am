import sys; input = sys.stdin.readline
n,m = map(int,input().split())
n_num = list(map(int,input().split()))
prefix = [0] * (n + 1)
for i in range(1,n+1):
    prefix[i] = prefix[i-1] + n_num[i-1]
for i in range(m):
    f,g = map(int,input().split())
    print(prefix[g] - prefix[f-1])