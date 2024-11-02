# n은 입력받는 숫자의 갯수 , m은 리미트 숫자
n,m = map(int,input().split()) 
# 숫자 입력 
numbers = list(map(int,input().split()))
# 결과값 설정
max_count = 0

# 반복문 시작
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if numbers[i]+numbers[j]+numbers[k] <= m:
                max_count = max(max_count,numbers[i]+numbers[j]+numbers[k])

print(max_count)