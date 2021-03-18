from tkinter import *
from tkinter import messagebox
#创建窗口对象
root = Tk()
#按钮
btn1 = Button(root)
#按钮显示
btn1['text'] = "点我就送花"
#压缩窗口
btn1.pack()

def songhua(e):   #事件对象e
    messagebox.showinfo("message",'送你一朵花')#message 标题
    print("送你九九朵花")

btn1.bind("<Button-1>",songhua)
#显示窗口(调用mainloop方法，进入事件循环)
root.mainloop()