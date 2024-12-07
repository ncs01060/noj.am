import sys; input = sys.stdin.readline
n,m = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

result = a-b

if result:
    print(len(result))
    print(*sorted(list(result)))
else:
    print(0)