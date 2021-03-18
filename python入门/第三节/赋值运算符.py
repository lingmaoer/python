# 赋值运算符 从右到左
i = 3 + 4
print(i)

a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

print("-------支持参数赋值------")
a = 20
a += 30
print(a)
a -= 10
print(a)
a *= 2
print(a)
a /= 3
print(a)
a //= 2
print(a)
a %= 3
print(a)

print("--------解包赋值------")
a, b, c = 10, 20, 30
print(a, b, c)

print("--------交换两个变量的值--------")
# 交换
a, b = 10, 20
a, b = b, a
