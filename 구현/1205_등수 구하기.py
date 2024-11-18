# n = 리스트의 개수
# m = 태수의 새로운 점수
# p = 최소 랭킹 등록 기준
n,m,p = map(int,input().split())
if n == 0:
    print(1)

else:
    num_list = list(map(int,input().split()))


    if m <= min(num_list) and len(num_list) == p:
        print(-1)
    else:
        rank = 1
        for i in range(n):
            if num_list[i] > m:
                rank += 1
            elif num_list == m:
                continue

        print(rank)