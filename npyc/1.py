n = int(input())
jobs = []
for i in range(n):
    job = input()
    jobs.append(job)

k = int(input())
alreadyJobs = []
for i in range(k):
    job = input()
    alreadyJobs.append(job)

result = [x for x in jobs if x not in alreadyJobs]
        

print(len(result))
for i in result:
    print(i)