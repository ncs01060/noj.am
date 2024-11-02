# 숫자 입력
n=int(input())

# 문자 입력

origin = input()

# 사전 변수
r = 31
m = 1234567891

result = 0

# 반복문 시작

for i in range(0,len(origin)):
    # a,b,c 문자열의 위치 값
    ord_str = ord(origin[i]) - 96

    # 결과값 = 위치 값 * r의 index 제곱
    result += ord_str * r ** i

# mod M 은 m을 나눈 나머지
print(result % m)