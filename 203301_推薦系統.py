import pprint as pp

decide = int(input())

d = {}
while True:
    ppl = input().split()
    if ppl[0] == 'end':
        break
    else:
        temp = sorted(ppl[1:])
        d[ppl[0]] = temp

pp.pprint(d)

def 
for key, value in d.items():
    