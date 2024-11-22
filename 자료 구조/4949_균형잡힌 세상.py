while True:
    msg = input()
    if msg == '.':
        break

    stack = []
    balenced = True

    for i in msg:
        if i in "([":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balenced = False
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balenced = False
                break
    
    if balenced and not stack:
        print('yes')
    else:
        print('no')
