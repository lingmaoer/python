# 组件对象的绑定
# Button(root,text="登录"，command=login)

# 通过bind（）方法绑定
# c1=Canvas()
# c1.bind('<Button-1>',drawLine)

#组件类的绑定
# w.bind_class("Widget",'event',eventhanler)

from tkinter import *

root=Tk()
root.geometry("270x30")

def mousetest1(event):
    print("bind()绑定，可以获取event对象")
    print(event.widget)

def mousetest2(a,b):
    print('a={0},b={1}'.format(a,b))
    print("command方式绑定，不能直接获取event对象")

def mousetest3(event):
    print("右键单击事件，绑定所有按钮了！！！")
    print(event.widget)

b1=Button(root,text='测试bind（）绑定')
b1.pack(side='left')
# bind()方式绑定
b1.bind("<Button-1>",mousetest1)

# command方式绑定
b2=Button(root,text='测试command',command=lambda :mousetest2("cccccccc",'aaaaaa'))
b2.pack(side="left")

#绑定所有按钮
b1.bind_class("Button","<Button-3>",mousetest3)

root.mainloop()