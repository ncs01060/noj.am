num1,num2 = map(int,input().split())

def greatest_divisor(num1:int,num2:int):
    max_divisor = 0
    
    for i in range(1,min(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            max_divisor = max(max_divisor,i)
    
    return max_divisor


def minist_divisor(num1:int,num2:int):

    for i in range(max(num1,num2),(num1 * num2)+1):
        if i % num1 == 0 and i % num2 == 0:
            return i

print(greatest_divisor(num1,num2))
print(minist_divisor(num1,num2))