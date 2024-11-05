# h = 세로
# w = 가로
# m = 세로 거리두기 길이
# n = 가로 거리두기 길이
import math
import sys; input = sys.stdin.readline
h,w,m,n = map(int,input().split()) 

countx = 0
county = 0

for i in range(0,h,m+1):
    countx+=1

for i in range(0,w,n+1):
    county+=1

print(countx * county)


