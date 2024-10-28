
t=int(input())
dp = [0]*301
step = [0]*301
for i in range(1,t+1):
    step[i] = int(input())
dp[1] = step[1]
dp[2] = step[1] + step[2]
dp[3] = max(step[1]+step[3],step[2]+step[3])

for i in range(4,t + 1):
    dp[i] = max(dp[i-3] + step[i-1] + step[i],dp[i-2] + step[i])

print(dp[t])