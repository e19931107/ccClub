for i in range(1,int(input())+1):
    if i%3 != 0 and i%5 != 0:
        print(i)
    elif i%3 == 0 and i%5 != 0:
        print('拍手')
    elif i%5 == 0 and i%3 != 0:
        print('拍頭')
    elif i%3 == 0 and i%5 == 0:
        print('拍手拍頭')