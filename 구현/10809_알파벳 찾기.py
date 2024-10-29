s=input()

word = [-1] * 26

for i in range(0,len(s)):
    if word[ord(s[i])-97] == -1:
        word[ord(s[i])-97] = i

print(*word)