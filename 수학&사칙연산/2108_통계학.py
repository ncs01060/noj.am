from collections import Counter
import sys; input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
num_list = [0 for _ in range(4000)]
print(round(sum(l)/len(l)))
ls = sorted(l)
if len(ls)%2 == 0:
    print(ls[len(ls)//2])
else:
    print(ls[(len(ls))//2])

counter = Counter(l)
max_frequency = max(counter.values())
modes = sorted([num for num, freq in counter.items() if freq == max_frequency])
if len(modes) < 2:
    print(modes[0])
else:
    print(modes[1])

print(max(l) - min(l))