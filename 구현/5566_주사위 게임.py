n,m = map(int,input().split())

board = [int(input()) for _ in range(n)]
dice = [int(input()) for _ in range(m)]

cnt = 0
now = 0
for i in range(m):
    cnt += 1
    now += dice[i]
    print("dice[i] : %d"%now)
    if now >= n:
        break
    now += board[now]
    if now >= n:
        break
    print("board[now] : %d"%now)

print(cnt)
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())   # m: 주사위 던진 횟수
bord = [int(input()) for _ in range(n)]   # 보드 각 칸의 지시 사항
dice = [int(input()) for _ in range(m)]   # 던져서 나온 주사위 번호

now = 0   # 현재 위치 index
cnt = 0   # 주사위 던진 횟수

for i in range(m):
  cnt += 1
  now += dice[i]
  if now >= n-1:
    break
  now += bord[now]
  if now >= n-1:
    break

print(cnt)
'''