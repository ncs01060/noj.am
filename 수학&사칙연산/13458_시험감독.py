n = int(input())
A_list = list(map(int,input().split()))
b,c=map(int,input().split())

AllViewer = 0
viewer = 0
cnt = 0
for box in A_list:
        cnt = box - b
        AllViewer+=1
        if cnt > 0:
              viewer += cnt//c
              if cnt % c > 0:
                 viewer += 1
            
print(viewer+AllViewer)  

'''
n = int(input())

a = list(map(int, input().split()))

b, c = map(int, input().split())

result = 0


for student in a:
    student = student - b
    result += 1

    if student > 0:
        result += student // c

        if student % c > 0:
            result += 1


print(result)
'''
