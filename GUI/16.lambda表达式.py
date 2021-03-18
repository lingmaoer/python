# lambda 参数值列表：表达式
# add=lambda x,y,z:x+y+z
# print(add(1,2,3))

from tkinter import *

root=Tk()
root.geometry("500x300")

def mouseTest1():
    print("command方式简单情况:不涉及获取event对象，可以使用")

def mouseTest2(a,b) :
    print ("a={0},b={1}".format (a, b))

Button( root, text ="测试command1" ,command=mouseTest1) .pack(side="left")

Button( root, text=" 测试command2" ,command= lambda: mouseTest2("gaogi", "xixi") ) .pack(side="left" )

root.mainloop()








