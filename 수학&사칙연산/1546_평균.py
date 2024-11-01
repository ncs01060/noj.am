n=int(input())
num = list(map(int,input().split()))
new = []
high = max(num)

for i in num:
    new.append(i/high*100)

print(sum(new) / n)