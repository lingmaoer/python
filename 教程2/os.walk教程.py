import os

path = os.getcwd()
list_files = os.walk(path)

for dirpath,dirnames,filenames in list_files:

    #目录
    for dirname in dirnames:
        # print(dirname)
        print(os.path.join(dirpath,dirname))

    #文件名
    for filename in filenames:
        # print(filename)
        print(os.path.join(dirpath,filename))