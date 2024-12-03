n = int(input())
computer = [0 for _ in range(100)]
person = list(map(int,input().split()))
cnt = 0
for i in person:
    if computer[i-1] == 1:
         cnt+=1
    else:
         computer[i-1] = 1

print(cnt)