n=int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

for i in sorted(words,key=lambda x: len(x[0])):
    print(i)

print(words)




    