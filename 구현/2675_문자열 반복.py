t=int(input())
for i in range(t):

    num,string = input().split()

    for j in string:
        print(j * int(num),end="") 
    print()
