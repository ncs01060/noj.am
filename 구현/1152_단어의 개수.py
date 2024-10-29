text= input()
sw =False
cnt = 0
for i in text:
    if i == " ":
        sw = True
    elif i != " " and sw == True:
        cnt += 1
        sw = False
if text[0] != " ":
    print(cnt+1)
else:
    print(cnt)
