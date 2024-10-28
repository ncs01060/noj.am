n, k = map(int, input().split())
board = [[0] * n for _ in range(n)]

for i in range(k):
    x, y, p = map(int, input().split())
    x -= 1
    y -= 1
    for dx in range(-p, p + 1):
        if 0 <= x + dx < n:
            board[y][x + dx] = 1
    for dy in range(-p, p + 1):
        if 0 <= y + dy < n:
            board[y + dy][x] = 1

zero_count = sum(row.count(0) for row in board)

print(zero_count)
