'''
data = open("yesterday").read()
print(data)
'''

'''
f = open("yesterday",encoding="utf-8")
data = f.read()
print(data)
f.close()
'''

'''
f = open("yesterday2",'w')
f.write("我爱北京天安门，\n")
f.write("天安门上太阳升。\n")
f.close()
'''

'''
f = open("yesterday2",'a')
f.write("我爱北京天安门，\n")
f.write("天安门上太阳升。\n")
f.close()
'''

'''
f = open("yesterday2",'r')
    for i in f:
        print(i)
for i in f.readlines():
    print(i.strip())
#strip 去掉换行和空格
#print(f.readline())
#c
f.close()
'''

'''
f = open("yesterday2",'r')
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())
f.close()
'''

'''
f = open("yesterday2",'r')
print(f.encoding)
'''

'''
import sys,time
for i in range(101):
    sys.stdout.write('%d%%'%(i))
    sys.stdout.flush()
    time.sleep(0.1)
'''

'''
f = open("yesterday2",'a',encoding='utf-8')
f.seek(10)
f.truncate(10)#截断
'''

'''
f = open("yesterday2",'r+',encoding='utf-8')#读写
f = open("yesterday2",'w+',encoding='utf-8')#写读
f = open("yesterday2",'a+',encoding='utf-8')#追加读
f = open("yesterday2",'wb',encoding='utf-8')#
f = open("yesterday2",'rb',encoding='utf-8')#二进制文件
f = open("yesterday2",'ab',encoding='utf-8')#
'''

#文件修改

'''
f = open("yesterday","r",encoding="utf-8")
f_new = open("yesterday3","w",encoding="utf-8")
for line in f:
    if "现在知道错在自己\n" in line:
        line = line.replace("现在知道错在自己\n","现在知道错在自己-----------\n")
    f_new.write(line)
f.close()
f_new.close()
'''


'''
# encode  编码
# decode  解码
import sys
print(sys.getdefaultencoding())
s = "你好"
s_to_unicode = s.encode("utf-8")
s_to_gbk = s_to_unicode.decode("utf-8")
s_to_gbk1 = s_to_gbk.encode("gbk")
s_to_gbk2 = s_to_gbk1.decode("gbk")
print(s_to_unicode)
print(s_to_gbk)
print(s_to_gbk1)
print(s_to_gbk2)
'''

# os   模块
# import os
# 重命名
# os.rename("原文件名", '新文件名')
# 删除文件
# os.remove("文件名")
# 查看内容  .是当前内容
# os.listdir(".")
# 判断是否文件
# os.path.isdir("")
# 创建文件
# os.mkdir("名字")
# 删除文件
# os.rmdir("名字")