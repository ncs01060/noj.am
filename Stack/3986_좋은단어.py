n=int(input())
cnt = 0
stack = []

for i in range(n):
    word = input()
    k=0
    sw = False
    while len(word) != k:
        if not len(stack):
            stack.append(word[k])
        elif stack[-1] == word[k]:
                stack.pop()
        else:
             stack.append(word[k])
        k+=1
    if not len(stack):
         cnt+=1
    stack = []
print(cnt)



