while True:
    n = input()
    if n == '0':
        break
    
    if n == n[::-1]:
        print('yes')
    elif n != n[::-1]:
        print('no')