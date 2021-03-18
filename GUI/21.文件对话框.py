"""文件对话框获取文件"""

# from tkinter import  *
# from tkinter.filedialog import *
#
# root = Tk();root.geometry("400x100")
#
#
# def test1():
#     f = askopenfilename(title="上传文件",
#                         initialdir="f:",filetypes=[("视频文件",".mp4")])
#     #print(f)
#     show["text"]=f
#
#
# Button(root,text="选择编辑的视频文件",command=test1).pack()
#
# show = Label(root,width=40,height=3,bg="green")
# show.pack()
#
# root.mainloop()


#coding=utf-8
#askcolor颜色选择框的测试，改变背景色

from tkinter import  *
from tkinter.filedialog import *

root = Tk();root.geometry("400x100")

def test1():
    with askopenfile(title="上传文件",
                     initialdir="d:",filetypes=[("文本文件",".txt")]) as f:
        show["text"]=f.read()


Button(root,text="选择读取的文本文件",command=test1).pack()

show = Label(root,width=40,height=3,bg="green")
show.pack()

root.mainloop()
