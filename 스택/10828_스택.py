import sys;input=sys.stdin.readline
stack = []
n = int(input())
for i in range(n):
    command = list(map(str,input().split()))
    if len(command) == 2:
        stack.append(int(command[1]))
    else:
        if command[0] == "pop":
            if stack:
                print(stack[-1])
                stack.pop()
            else:
                print(-1)
        elif command[0] == "size":
            print(len(stack))
        elif command[0] == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif command[0] == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)

        