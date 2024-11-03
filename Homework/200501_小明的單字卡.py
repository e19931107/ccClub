c_to_e = {}
e_to_c = {}

while True:
    x = input().split()
    if x[0] == 'I':
        if x[1] not in c_to_e:
            e_to_c[x[2]] = x[1]
            c_to_e[x[1]] = x[2]
            print('[succeed]')
        else:
            print('[fail]')
    elif x[0] == 'C':
        print(c_to_e.get(x[1],'[fail]'))
    elif x[0] == 'E':
        print(e_to_c.get(x[1],'[fail]'))
    else:
        break