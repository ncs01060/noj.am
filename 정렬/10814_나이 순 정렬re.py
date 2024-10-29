'''
n=int(input())
player = []

for i in range(n):
    age,name = input().split()
    player.append([int(age),name])


for i in sorted(player,key=lambda x: x[0]):
    print(i[0],i[1])

'''


n=int(input())
player = []
for i in range(n):
    age,name = input().split()
    player.append([int(age),name])

for i in sorted(player, key=lambda x: x[0]):
    print(*i)
    