t=int(input())
for i in range(t):
    count = 0
    n,k=map(int,input().split())
    candy_list = list(map(int,input().split()))
    for i in range(n):
        count += candy_list[i] // k
    print(count)
