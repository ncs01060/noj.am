n,m = map(int,input().split())
dp = [_ for _ in range(1,n+1)]
new_dp = set()

for i in range(m):
    cnt = 0
    a,b = map(int,input().split())


    for j in range(a,b):
        new_dp.add(dp[j]**2)
        for k in range(a,b):
            new_dp.add(dp[j] * dp[k])

    
    for k in new_dp:
        if k >= a and k <= b:
            cnt+=1
    print(cnt)


ls = sorted(list(new_dp))
print(cnt)