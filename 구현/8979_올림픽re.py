N,K = map(int,input().split())
ranks = []
for i in range(N):
    rank = list(map(int,input().split()))

result = 1
max_result = 0
for i in ranks:
    if i[0] == K:
        max_result = i

for i in range(1,4):
    result+=1
    cnt = 0
    for j in range(len(ranks)):
        if ranks[j][i] > max_result[i]:
            cnt+=1
    if cnt == 0:
        break
print(result)