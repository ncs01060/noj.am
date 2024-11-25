n = int(input())
cnt = 0
for si in range(0,n+1):
    for bun in range(0,60):
        for cho in range(0,60):
            if '3' in str(si) or '3' in str(bun) or '3' in str(cho):
                cnt += 1
print(cnt)