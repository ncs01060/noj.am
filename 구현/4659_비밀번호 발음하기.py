importent = ['a','e','i','o','u']
while True:
    check = [False,True,True]
    gather_count = 0
    not_gather_count = 0
    double_check = 0
    st = input()
    if st == 'end':
        break
    for i in st:

        if i in importent:
            check[0] = True
            not_gather_count = 0
            gather_count+=1
            if gather_count >= 3:
                check[1] = False
        else:
            gather_count = 0
            not_gather_count+=1
            if not_gather_count >= 3:
                check[2] = False
    if check[0] == True and check[1] == True and check[2] == True:
        for i in range(1,len(st)):
            if st[i-1] == st[i] and st[i] != 'e' and st[i] != 'o':
                double_check+=1
            if double_check >= 1:
                check[2] = False
                break
    if check[0] == True and check[1] == True and check[2] == True:
        print(f"<{st}> is acceptable.")
    else:
        print(f"<{st}> is not acceptable.")