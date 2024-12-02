a,b,c = map(int,input().split())
strs = str(a/b)
cnt = 0
sw = False
print(strs)
for i in strs:
    if i == '.':
        cnt = 0
    elif cnt == c:
        print(i)
        break
    cnt+=1
