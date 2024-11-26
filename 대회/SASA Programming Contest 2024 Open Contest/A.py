k = input().split()
cnt = float(k[0])
for i in range(1, len(k), 2): 
    operator = k[i]
    operand = float(k[i + 1])
    if operator == "+":
        cnt += operand
    elif operator == "-":
        cnt -= operand
    elif operator == "*":
        cnt *= operand
    elif operator == "/":
        cnt /= operand
result = round(cnt, 3)
print("=================")
print("|SASA CALCULATOR|")
print(f"|  {result:>13.3f}|")
print("-----------------")
print("|               |")
print("| AC         /  |")
print("| 7  8  9    *  |")
print("| 4  5  6    -  |")
print("| 1  2  3    +  |")
print("|    0  .    =  |")
print("=================")