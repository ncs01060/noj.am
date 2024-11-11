playBoard = {"Y":2,"F":3,"O":4}
player = set()
N,Play = input().split()
for i in range(int(N)):
    name = input()
    player.add(name)
need_player = playBoard[Play]
print(len(player) // (need_player-1))
