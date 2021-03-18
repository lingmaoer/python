s = 'hello,python'
# 字符串是否合法标识符
print('1.', s.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', '张三_'.isidentifier())
print('4.', '张三_123'.isidentifier())

# 字符串是否都是空格
print('5.', ' \t\n'.isspace())
print('6.', ' 1\t\n'.isspace())

#字符串是否都是字母
print('7.', 'weds'.isalpha())
print('8.', '张三'.isalpha())
print('9.', '张三1'.isalpha())

#字符串是否十进制数字组成
print('10.', '123'.isdecimal())
print('11.', '123四'.isdecimal())

# 字符串是否全部由数字组成（罗马数字也是）
print('12.','123'.isnumeric())
print('12.','123四'.isnumeric())

# 是否全部由字母和数字组成
print('15.','abc1'.isalnum())
print('15.','张三123'.isalnum())
print('15.','abc1!'.isalnum())
