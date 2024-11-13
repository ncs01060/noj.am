import sys; input = sys.stdin.readline
n=int(input())
nums = [0] * 10001

for i in range(n):
    num = int(input())
    nums[num] += 1


for i in range(0,len(nums)):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)
