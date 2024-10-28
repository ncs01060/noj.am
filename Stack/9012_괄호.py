n=int(input())
stack = []
for i in range(n):
    VPS = 0

    text = input()
    for j in text:
        stack.append(j)
    
    for j in range(len(stack)+1):
        if stack and stack[0] == "(":
            VPS += 1
            stack.pop(0)
        elif stack and VPS != 0 and stack[0] == ")":
            VPS-=1
            stack.pop(0)
    if stack or VPS > 0:
        print("NO")
    else:
        print("YES")
    stack = []
        

