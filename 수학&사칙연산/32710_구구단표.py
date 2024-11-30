n = int(input())
sw = False
for i in range(2,10):
    for j in range(1,10):
        if i * j == n or i == n or j == n:
            sw = True
            break
    
if sw:
    print(1)
else:
    print(0)