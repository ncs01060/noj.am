n = int(input())
students = []
max_grade_count = 0
num = 0
for i in range(n):
    students.append(list(map(int,input().split())))


for i in range(0,n):
    grade_count = 0
    for j in range(0,n):
        for k in range(5):

            if students[i][k] == students[j][k]:
                grade_count+=1
                break
    
    if max_grade_count < grade_count:
        max_grade_count = grade_count
        num = i

print(num+1)