n=int(input())
aver_list = []
for i in range(n):
    k = int(input())
    aver_list.append(k)

none = round(n*0.15)


for i in range(0,none):
    del aver_list[i]

print(aver_list)
aver_list = aver_list[::-1]

for i in range(0,none):
    del aver_list[i]

count = sum(aver_list)/len(aver_list)

print(aver_list)
    