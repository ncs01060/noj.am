# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다 (단 나누어 떨어지는 경우만 가능)

n,k = map(int,input().split())
count = 0
while n > 1:
    if n%k == 0:
        n = n//k
        count+=1
    else:
        n-=1
        count+=1
print(count)

