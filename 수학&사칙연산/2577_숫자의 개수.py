a=int(input())
b=int(input())
c=int(input())
k = [0]*10
result = a*b*c 

for i in str(result):
    k[int(i)]+=1


for i in k:
    print(i)