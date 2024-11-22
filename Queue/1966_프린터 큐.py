from collections import deque

n=int(input())
for i in range(0,n):

    queue = deque()
    temp = deque()
    n,m=map(int,input().split())
    l = list(map(int,input().split()))
    queue.extend(l)
    tmp = queue[m]
    temp.extend(l)
    cnt = 0
    tm_count = 0
    m_count = 0
    for j in range(0,len(queue)): # 큰 값이 정해져 있는경우
        if max(queue) == tmp:
            cnt += 1
            break
        else:
            cnt+=1
            queue.remove(max(queue))

    for j in range(0,len(queue)):
        if tmp == queue[j]:
            tm_count += 1
    if tm_count >= 2:
        #cnt = (len(queue)-queue.index(max(queue))-1) + m+1
        j=0
        while True:
            if temp[j] == max(temp):
                temp.remove(max(temp))
                if  max(temp) == tmp:
                    cnt+=m_count
                    break
            temp.append(temp.popleft())
            m_count += 1
            

    print(cnt)


