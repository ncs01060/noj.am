import sys;input = sys.stdin.readline
from collections import deque
n = int(input())
nums = deque(_ for _ in range(1,n+1))

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())
print(*nums)