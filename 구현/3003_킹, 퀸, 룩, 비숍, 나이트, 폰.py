need_chess = [1,1,2,2,2,8]
chess = list(map(int,input().split()))
result = []
for i in range(len(chess)):
    result.append(need_chess[i] - chess[i])

print(*result)