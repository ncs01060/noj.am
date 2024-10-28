import sys
input = sys.stdin.readline
n,k=map(int,input().split()) # n 갯수 k 버틸 수 있는 무게
items = []
for _ in range(0,n):
    wv= list(map(int,input().split()))
    items.append(wv)

result = 0

for i in range(0,len(items)):
    weights = items[i][0]
    value = items[i][1]
    for j in range(0,len(items)):
        if i==j:
            pass
        elif weights + items[j][0] > k:
            weights = items[i][0]
            value = items[i][1]
        else:
            print(f"origin value is : {value}")
            weights += items[j][0]
            value += items[j][1]
            print(f"plus value is : {value}")
            result = max(result,value)

print(result)