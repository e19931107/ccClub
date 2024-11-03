import re
word = input().split()
word = sorted(word, key = len, reverse = True)
# print(word)

while True:
    text = input()
    if text == 'end':
        break
    
    lst = []
    for i in word:
        print(i)
        if re.search(i, text):
            lst.append(re.search(i, text).span())
    print(lst)

    
        