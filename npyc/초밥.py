
T = int(input())


for _ in range(T):
    A, B = map(int, input().split())
    count = 0
    if B > A:
        A,B = B,A
    
    while B > 0 or A > 0:
        if B > 0 and B < A:
            B -= 1
            A-=3
            count+=1
        elif B > 0 and B > A:
            B -= 3
            A -= 1
            count+=1
        elif A == B:
            A-=2
            B-=2
            count+=1
        else:
            count = -1
            break
    print(count)
    

