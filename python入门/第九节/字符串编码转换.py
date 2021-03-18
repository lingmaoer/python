s = '天涯共此时'
# 编码
print(s.encode(encoding='GBK'))  # 在GBK这种编码格中一个中文占两个字节

print(s.encode(encoding='utf-8'))  # 在utf-8这种编码格中一个中文占三个字节

# 解码
byte = s.encode(encoding='utf-8')
print(byte.decode(encoding='utf-8'))

byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
