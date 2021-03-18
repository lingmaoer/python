# 将指定的十进制数转换成二进制、八进制、十六进制
num = int(input("输入一个十进制整数："))
print(num, '的二进制数为:', bin(num))  # 第一种写法，使用了个数可变的位置参数
print(str(num) + '的二进制数为:' + bin(num))  # 第二种写法，使用"+"作为连接符﹒(+的左右均为str类型)
print('%s的二进制数为:%s' % (num, bin(num)))  # 第三种写法，格式化字符串
print('{0}的二进制数为:{1}'.format(num, bin(num)))  # 第三种写法，格式化字符串
print(f'{num}的二进制数为:{bin(num)}')  # 第三种写


print(num, "的八进制数为", oct(num))
print(num, "的十六进制数为", hex(num))
