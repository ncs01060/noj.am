n = int(input())
for i in range(n):
    num = list(map(int,input().split()))
    max_cnt = 0
    while True:
        cnt = 0

        for i in range(2,len(num)):
            if num[i] < num [i-1]:
                num[i],num[i-1] = num[i-1],num[i]
                cnt+=1
        max_cnt+=cnt
        if cnt == 0:
            break 
    print(num[0],max_cnt)