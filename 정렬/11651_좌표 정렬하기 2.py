n=int(input())
xyz = []
for i in range(n):
    x=list(map(int,input().split()))
    xyz.append(x)


xyz.sort(key = lambda x: x[0])

for i in xyz:
    for j in i:
        print(j,end=" ")
    print()
