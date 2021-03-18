print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'),ord('b'),ord('谢'))
print(chr(97), chr(98),chr(35874))

# ==  与  is的区别
# ==比较的是value
# is比较的是id 是否相等
a=b='python'
c='python'
print(a==b)
print(b==c)

print(a is b)
print(b is c)

print(id(a),id(b),id(c))