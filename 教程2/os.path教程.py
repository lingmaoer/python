#!coding=utf-8
from os import path
import os

#判断是否绝对路径
# path.isabs(path)

#判断是否为目录
# path.isdir(path)

#判断是否为文件
# path.isfile(path)

#判断指定文件是否存在
# path.exists(path)

#返回文件大小
# path.getsize(filename)

#返回绝对路径
# path.abspath(path)

#返回目录的路径
# path.dirname(path)

#返回文件的最后访问时间
# path.getatime(filename)

#返回文件的最后修改时间
# path.getmtime(filename)

#递归方式遍历目录
# path.walk()

#连接多个path
# path.join(path,*paths)

#对路径进行分割，以列表形式返回
# path.split(path)

#从路径分割文件的拓展名
# path.splitext()

path = os.getcwd()
# print(path)
file_list = os.listdir(path)
for filename in file_list:
    if filename.endswith('py'):
        print(filename)

file_list2 = [filename for filename in os.listdir(path) if filename.endswith('py')]
print(file_list2)