s = input()
cnt = 1
for i in s:
    if i == '0' or i == '1':
        cnt+=int(i)
    else:
        cnt*=int(i)

print(cnt)