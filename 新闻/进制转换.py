def to_ten():
    zidian = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    zhengshu = 0
    xiaoshu = 0
    a = input("输入表达式：")
    jinzhi = int(input("输入进制"))
    flag = 0
    c = a.split('.')
    # print(c)
    for i in c[0][::-1]:
        i = zidian[i]
        zhengshu += i * jinzhi ** flag
        flag += 1
    flag = -1
    for i in c[1]:
        xiaoshu += int(i) * jinzhi ** flag
        flag -= 1

    print(zhengshu + xiaoshu)


def to_othernum():
    zidian = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
              9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    zhengshu = []
    xiaoshu = []
    a = input("输入表达式：")
    jinzhi = int(input("输入进制"))
    flag = 0
    c = a.split('.')
    str1 = ''
    # print(c)
    num = int(c[0])
    i = zidian[num % jinzhi]
    zhengshu.append(i)
    while num // jinzhi != 0:
        num //= jinzhi
        i = zidian[num % jinzhi]
        zhengshu.append(i)

    str2 = '0.' + c[1]
    num = float(str2)

    while num * jinzhi != 0:
        num *= jinzhi
        i = zidian[int(num // 1)]
        xiaoshu.append(i)
        if num >= 1:
            num -= int(num // 1)
        flag += 1
        if flag == 10:
            break
    zhengshu.reverse()
    for i in zhengshu:
        str1 += str(i)
    str1 += '.'
    if xiaoshu == []:
        str1 += '0'
    else:
        for i in xiaoshu:
            str1 += str(i)
    for i in str1:
        print(i, end='')
    print('\n')


while True:
    print("1.其他进制转十进制（主要是2，8）：")
    print("2.十进制转其他进制（主要是2，8）：")
    num = int(input("输入选择"))
    if num == 1:
        to_ten()
    elif num == 2:
        to_othernum()
    else:
        pass


