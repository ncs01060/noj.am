import sys;input = sys.stdin.readline
N, L, R = map(int, input().split())
fx = list(map(int, input().split()))
fx[L-1:R] = sorted(fx[L-1:R])
last_num = fx[L-2] # 1 
is_increasing = True

for i in fx:
    if last_num > i:
        is_increasing = False
        break
    last_num = i

if is_increasing:
    print(1)
else:
    print(0)

    
