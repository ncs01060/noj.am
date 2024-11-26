n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
money = k
coin = 0

for i in range(n):
    if coins[i] <= money:
        coin+=(money // coins[i])
        money = money - (money // coins[i]) * coins[i]
        
print(coin)