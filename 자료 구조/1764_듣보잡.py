n,m=map(int,input().split())
current_player =set(input() for _ in range(n))
check_player = [input() for _ in range(m)]

cnt = 0
realPlayer = []
for i in range(m):
    if check_player[i] in current_player:
        cnt+=1
        realPlayer.append(check_player[i])

print(cnt)
for i in sorted(realPlayer):
    print(i)