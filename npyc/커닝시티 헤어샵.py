def min_total_service_time(service_times):
    n = len(service_times)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0 
    
    for i in range(1, n + 1):
        # Case 1: Single customer
        dp[i] = dp[i - 1] + service_times[i - 1]
        # Case 2: Two customers at once
        if i > 1:
            dp[i] = min(dp[i], dp[i - 2] + max(service_times[i - 1], service_times[i - 2]))
    
    return dp[n]
n = int(input())
service_times = list(map(int, input().split()))
result = min_total_service_time(service_times)
print(result)
