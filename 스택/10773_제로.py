import sys;input = sys.stdin.readline
k = int(input())
nums = []
for i in range(k):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
    
print(sum(nums))