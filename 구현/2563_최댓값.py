number = []
for i in range(0,9):
    a=int(input())
    number.append(a)
print(max(number))
print(number.index(max(number))+1)