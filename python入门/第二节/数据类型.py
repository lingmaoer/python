# 整数，复数，0
n1 = 9
n2 = -10
n3 = 0
print(type(n1))
print(type(n2))
print(type(n3))

# 整数可以表示为二进制，十进制，八进制，十六进制
print('十进制', 1188)
print('二进制', 0b110010)
print('八进制', 0o1642)
print('十六进制', 0x1642)

# 浮点类型
a = 3.14159
print(a, type(a))
n4 = 1.1
n5 = 2.2
n6 = 3.3
from decimal import Decimal

print(Decimal("1.1") + Decimal("2.2"))
print(n4 + n6)

f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))
print(f1 + 1)
print(f2 + 1)

# 字符串类型
str1 = "人生苦短，我用python"
str2 = '人生苦短，我用python'
str3 = '''人生苦短，
        我用python'''
str4 = """人生苦短,
        我用python"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))