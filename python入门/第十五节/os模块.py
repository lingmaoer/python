import os
# os.system('notepad.exe')
# os.system('calc.exe')

# 直接调用可执行文件
# os.startfile('D:\\Software\\网易云音乐\\CloudMusic\\cloudmusic.exe')

print(os.getcwd())# 返回当前的工作目录
lst = os.listdir('../第十五节')#返回指定路径下的文件和目录信息
print(lst)

# os.mkdir('test')#创建目录
# os.makedirs('A/B/C')#创建多级目录
# os.rmdir('A/B')
# os.removedirs("A/B")

os.chdir("D:\\Software\\网易云音乐\\CloudMusic")
print(os.getcwd())