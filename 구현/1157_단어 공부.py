n=input()
lower_n = n.lower()

alph = [0 for _ in range(26)]


for i in lower_n:
    alph[ord(i)-97] += 1
cnt = 0
for i in range(0,len(alph)):
    if alph[i] != 0:
        if max(alph) == alph[i]:
            cnt+=1

if cnt >= 2:
    print("?")
else:
    print(chr(alph.index(max(alph))+97).upper())