n = int(input())
players = [list(map(int, input().split())) for _ in range(n)]
ranks = []

# 각 사람의 덩치 순위를 계산
for i in range(n):
    rank = 1
    for j in range(n):
        # 사람 i가 사람 j보다 덩치가 작으면
        if players[i][0] < players[j][0] and players[i][1] < players[j][1]:
            rank += 1  # 사람 i의 순위를 하나 증가시킴
    ranks.append(rank)

# 결과 출력
print(" ".join(map(str, ranks)))