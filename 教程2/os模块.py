import os

#打开记事本
# os.system('notepad.exe')
# os.system("ping www.baidu.com")
# os.system('cmd')


#直接调用可执行文件
# os.system(r'D:\Software\QQ\Bin\QQScLauncher.exe')

#删除指定文件
# os.remove(path=' ')

#重命名指定文件或目录
# os.rename(src=' ',dst= ' 0')

#返回文件的所有属性
# os.stat(path)

#返回path下的文件和目录列表
# os.listdir(path)

#创建目录
# os.mkdir(path)

#创建多级目录
# os.makedirs(path1/path2/path3)

#删除目录
# os.rmdir(path)

#删除多级目录  (空目录)
# os.removedirs(path1/path2/path3)

#返回当前工作目录
# os.getcwd()

#把path设为当前工作目录
# os.chdir(path)

#遍历目录树
# os.walk()

#当前操作系统所使用的路径分割符
# os.sep

#操作系统  windows -> nt   linux和unix->posix
print (os.name)
#   windows -> \   linux和unix-> /
print (os.sep)
#   windows -> \r\n  linux-> \n\
print (repr(os.linesep))