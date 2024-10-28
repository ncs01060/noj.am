n=int(input())
num = list(map(int,input().split()))

count = 0
for i in num:
    sw = False
    if i == 1:
        continue
    for j in range(2,i-1):
        if i%j == 0:
            sw = True
            break
    if sw == False:
        count+=1
print(count)