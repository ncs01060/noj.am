import sys
inpurt = sys.stdin.readline
N = int(input())
op = []
stack = []
temp = True
count = 1
for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break
if temp:
    for _ in op:
        print(_)
else:
    print("NO")
