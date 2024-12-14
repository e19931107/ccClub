x = input().split(',')
num = int(x[-1])
x = x[0:len(x)-1]
lst = input()
lst = [*lst]

direction = {'上':['上','下','左','右'],
             '下':['下','左','右','上'],
             '左':['左','右','上','下'],
             '右':['右','上','下','左']
             }

#字被置換的結果
new_word = {}
for i in x[0:len(x)]:
    new_word[i] = direction[i][num%4]
print(new_word)
#----------------------------------------------------------
#用enumerate賦予輸入串的位置
new_dic = {}
for i, j in enumerate(lst):
     new_dic[i] = j

#創造新的dictionary把置換的字放進去
answer = {}
for key, value in new_dic.items():
     for akey, avalue in new_word.items():
          if value == akey:
               answer[key] = avalue

for key, value in answer.items():
     new_dic.update({key:value})

print(''.join(str(final) for final in new_dic.values()))