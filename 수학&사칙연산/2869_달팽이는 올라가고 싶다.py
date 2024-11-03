# 하루에 올라가는 거리 a-b
# 올라가야하는 진짜 높이 v-b
a,b,v = map(int,input().split())
day = 0
line = 0


if (v-b) % (a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)