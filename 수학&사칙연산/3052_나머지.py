num_list = []
for i in range(10):
    n = int(input())
    num_list.append(n%42)


num_list = len(set(num_list))
print(num_list)