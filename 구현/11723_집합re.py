import sys ; input = sys.stdin.readline
s = set()


n = int(input())
for i in range(n):
    num_list = list(map(str,input().split()))
    if len(num_list) == 1:
        if num_list[0] == "all":
         s = set(list(range(1,21)))
        elif num_list[0] == "empty":
                s = set()
    else:
        command, num = num_list[0], num_list[1]
        x = int(num)

        if command == "add":
            s.add(x)
        elif command == "remove":
            s.discard(x)
        elif command == "check":
            print(1 if x in s else 0)
        elif command == "toggle":
            (s.discard(x) if x in s else s.add(x))
    
