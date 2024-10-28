'''

import sys
a=int(sys.stdin.readline())
Queue = []
for _ in range(a):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        Queue.insert(0, cmd[1])
    elif cmd[0] == "pop":
        if Queue:
            print(Queue.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(Queue))
    elif cmd[0] == "empty":
            if len(Queue) == 0:print(1)
            else:
                print(0)
    elif cmd[0] == "front":
        if Queue[0]:
            print( Queue[0])
        else:
            print(-1)
    else:
        if Queue[-1]:
            print(Queue[-1])
        else:
            print(-1)
      

import sys
N = int(sys.stdin.readline())
queue = []
for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.insert(0, cmd[1])
    elif cmd[0] == "pop":
        if len(queue) != 0: 
            print(queue.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if len(queue) == 0:
            print(1)
        else :
            print(0)
    elif cmd[0] == "front":
        if len(queue) == 0: print(-1)
        else:
            print(queue[len(queue) -1])
    elif cmd[0] == "back":
        if len(queue) == 0: print(-1)
        else:
            print(queue[0])
            '''

import sys
a=int(sys.stdin.readline())
Queue = []
for _ in range(a):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        Queue.insert(0,cmd[1])
    elif cmd[0] == "pop":
        if Queue:
            print(Queue.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(Queue))
    elif cmd[0] == "empty":
            if len(Queue) == 0:
                print(1)
            else:
                print(0)
    elif cmd[0] == "front":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[-1])
    elif cmd[0] == "back":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[0])