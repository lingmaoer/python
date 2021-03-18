# 转义字符
print("hello\nworld")  # \ +转义字符的首字符  n->newline
print("hello\tworld")
print("helloooo\tworld")
print("hello\rworld")  # 回车
print("hello\bworld")  # 退格

print("http:\\\\www.baidu.com")
print("老师说：\'大家好\'")

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r,或R
print(r"hello\nworld")
# 注意事项  最后不能是
