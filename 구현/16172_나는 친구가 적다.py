wrong_string = input()
find_string = input()
num = ["0","1","2","3","4","5","6","7","8","9"]
new = ""
for i in wrong_string:
    if i in num:
        continue
    new+=i

if find_string in new :
    print(1)
else:
    print(0)