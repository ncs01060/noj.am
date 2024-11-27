import sys; input = sys.stdin.readline


max_k = 40
dp = [(0,0)] * (max_k+1)
dp[0] = (1,0)
dp[1] = (0,1)

for i in range(2,max_k+1):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

n=int(input())
for i in range(n):
    k = int(input())
    print(dp[k][0],dp[k][1])