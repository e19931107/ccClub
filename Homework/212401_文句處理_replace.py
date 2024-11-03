word = input().split()
word = sorted(word, key = len, reverse = True)

dicti = {}
i = 1
for key in word:
    dicti['key'+str(i)] = key
    i += 1

# print(dicti)

while True:
    text = input()
    if text == 'end':
        break

    for key,value in dicti.items():
        text = text.replace(value, key)
    # print(text)

    for key, value in dicti.items():
        text = text.replace(key, '「'+value+'」')
    print(text)

