min_word = input()
add_word = input()

min_word = [ord(i)-96 for i in [*min_word]]
add_word = [ord(i)-96 for i in [*add_word]]
print(min_word)
print(add_word)

for index in range(len(min_word)):
    if index >= len(add_word) or index+1 >= len(add_word):
        temp = index%len(add_word)
        new = min_word[index]+add_word[index]+add_word[temp]
        print(chr(new+96))
    else:
        new = min_word[index]+add_word[index]+add_word[index+1]
        print(chr(new+96))

        