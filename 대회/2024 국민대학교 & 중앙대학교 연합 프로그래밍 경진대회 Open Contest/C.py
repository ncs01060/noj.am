N,K = map(int,input().split())
ls = []
if N == 1 and K == 2:
    print("1 1")

elif N == 1:
    for i in range(K):
        print(1,end=" ")


else:
    print(-1)
