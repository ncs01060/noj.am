def sorter(a: list):
    return sorted(a, key=lambda x: (len(x), x))


n = int(input())
words = set()

for i in range(n):
    word = input()
    words.add(word)

words = list(words)

for word in sorter(words):
    print(word)