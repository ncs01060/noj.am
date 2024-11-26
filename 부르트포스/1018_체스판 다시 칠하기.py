n,m = map(int,input().split())
board = []
for i in range(n):
    word = []
    k = input()
    for j in k:
        word.append(j)
    board.append(word)


cnt = 0
for i in range(0,n-1):
    for j in range(0,m-1):
        if board[i][j] == board[i][j+1]:
            cnt+=1
            if board[i][j] == 'W':
                board[i][j+1] = 'B'
            elif board[i][j] == 'B':
                board[i][j+1] = 'W'
        

print(cnt)