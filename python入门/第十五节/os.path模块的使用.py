import os.path

print(os.path.abspath('a.txt'))  # 绝对路径
print(os.path.exists('a.txt'), os.path.isdir('a.txt'))  # 是否存在，是否文件
print(os.path.join('e:python', 'copylogo.png'))  # 拼接（剪贴）
# print(os.path.split())  # 分离文件和文件夹
# print(os.path.splitext())  # 分离文件名和后缀
# print(os.path.basename())  # 从一个目录中提取文件名
# print(os.path.dirname())  # 从一个路径中提取文件路径，不包括文件名
# print(os.path.isdir())  # 用于于判断是否为路径
