n=int(input())
apples = []
for i in range(n):
    student,apple = map(int,input().split())
    apples.append(apple%student)

print(sum(apples))