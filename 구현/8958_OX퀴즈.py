n=int(input())

for i in range(n):
    ox = input()
    count = 1
    cnt = 0

    for j in ox:
        if j == "O":
            cnt+=count
            count += 1
        elif j == "X":
            count = 1
    print(cnt)
