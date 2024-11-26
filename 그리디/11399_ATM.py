n=int(input())
personal_time = list(map(int,input().split()))
personal_time.sort()
current_time = 0
result_time = 0
for i in range(n):
    current_time+=personal_time[i]
    result_time+=current_time
print(result_time)