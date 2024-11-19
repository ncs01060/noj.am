T = int(input())
for i in range(T):
    k = input()
    left = 0
    for i in k:
        if i == '(':
            left+=1
        elif i == ')':
            if left >= 1:
                left-=1
            else:

                left = 1
                break
    
        
    if left == 0 :
        print("YES")
    else:
        print("NO")