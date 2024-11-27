n = int(input())
dp = [0]*(10**6)
dp[0] = n

i = 1
cnt = 0
while True:
    if dp[i-1] == 1:
         break
    # 최적의 해를 구하는 솔루션이 필요함;;
    elif dp[i-1] % 3 == 0:
        dp[i] = dp[i-1] // 3
    elif dp[i-1] % 2 == 0:
            dp[i] = dp[i-1] // 2
    else:
         dp[i] = dp[i-1]-1
    i+=1
    cnt+=1

print(cnt)
print(dp[0:10])