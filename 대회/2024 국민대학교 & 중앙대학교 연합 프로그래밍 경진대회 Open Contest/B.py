import sys;input = sys.stdin.readline
N, L, R = map(int, input().split())
fx = list(map(int, input().split()))
fx[L-1:R] = sorted(fx[L-1:R])

if fx == sorted(fx):
    print(1)
else:
    print(0)

    
