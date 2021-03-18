from tkinter import *
from tkinter import messagebox

class Application(Frame):
    """一个经典GUI的类的写法"""
    def __init__(self,master=None):
        super().__init__(master)
        self.mastr = master
        self.pack()
        self.creatwidget()
    def creatwidget(self):
        """创建组件"""
        self.btn1=Button(self)
        self.btn1['text']='送花'
        self.btn1.pack()
        self.btn1['command'] = self.songhua
        #退出按钮
        self.btnquit = Button(self,text='退出',command=root.destroy)
        self.btnquit.pack()
    def songhua(self):
        messagebox.showinfo("送你一个🦔",'🐖🐖🐖')

root = Tk()
root.geometry("500x300+500+300")
root.title('一个经典GUI的类的写法')
app = Application(master = root)

root.mainloop()