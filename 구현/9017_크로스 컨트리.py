T = int(input())

for i in range(T):

    N = int(input())
    nums = list(map(int,input().split()))
    players = max(nums)
    count = 0
    points = [0] * players
    current_num = []
    point = [0] * players
    for i in range(N):
        point[nums[i]-1]+=1
    
    for i in range(0,len(point)):
        if point[i] < 6:
            current_num.append(i+1)
    poin = len(nums)
    for i in nums:
        if i in current_num:
            continue
        else:
            points[i-1] += poin
            print(poin) 
            poin-=1

print(points)


