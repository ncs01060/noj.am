iron_stick = input()
stack = []
cnt=0
for i in range(len(iron_stick)):
    if iron_stick[i] == "(":
        stack.append("(")
    else:
        if iron_stick[i-1] == "(":
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1

print(cnt)

        


