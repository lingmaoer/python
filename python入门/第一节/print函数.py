# 数字
print(520)
print(98.5)

# 字符串
print("hello world")
print('HELLO WORLD')

# 含有运算符的表达式
print(3+1)

# 将数据输出文件中 ,注意点，1，所指定的盘符在存在，2.使用file= fp
fp=open("./text.txt", 'w')
print("hello world",file=fp)
fp.close()

#不进行换行输出
print("hello", "world", "python")