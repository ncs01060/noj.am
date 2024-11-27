st_1 = input()
st_2 = input()

if len(st_1) > len(st_2):
    lang = st_1
    not_lang = st_2
    cha = len(st_1) - len(st_2)
else:
    lang = st_2
    not_lang = st_1
    cha = len(st_2) - len(st_1)

password = ""
lang = lang[cha:]
for i in range(len(lang)):
    if lang[i] == not_lang[i]:
        password+=lang[i]

print(password)