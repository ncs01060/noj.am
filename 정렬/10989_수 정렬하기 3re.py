# 계수정렬
import sys 
input = sys.stdin.readline
n=int(input())

count = [0]*10001 # 사전 리스트 만들기

for i in range(n):
    k = int(input())
    count[k] += 1 # 숫자마다의 인덱스에 +1

for i in range(1,10001):
    if count[i] != 0: # 0이 아니라면 인덱스 출력
        for _ in range(count[i]): # 여러개일 경우
            print(i)
