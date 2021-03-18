s = 'hello,python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
new_str = s1+s3+s2
print(new_str)

print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(new_str))
print(s[1:5:1])
print(s[::2])
print(s[::-1])
print(s[-6::1])

