while True:
    a,b,c = map(int,input().split())
    if a+b+c == 0:
        break
    large = max(a,b,c)
    first = min(a,b,c)
    mid = a+b+c-large-first
    if first**2+mid**2 == large**2:
        print("right")
    else:
        print("wrong")
