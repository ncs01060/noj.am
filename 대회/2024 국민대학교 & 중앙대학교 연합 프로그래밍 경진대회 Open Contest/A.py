n = int(input())
k = list(map(int,input().split()))
ham_num = input()
#a,b,c,d

if ham_num[0] != 'a' or ham_num[-1] != 'a':
    print("No")
else:
    lasat_ham_num = ''
    for i in ham_num:
        if lasat_ham_num == i:
            print("No")
            break
        if k[ord(i)-ord('a')] == 0:
            print("No")
            break
        k[ord(i)-ord('a')] -= 1
        lasat_ham_num = i
    
    else:
        print('Yes')