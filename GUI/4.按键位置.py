from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatwidget()

    def creatwidget(self):
        self.btn1=Button(root,text='登录',width=6,height=3,anchor=NE, command=self.login)#方向大写
        self.btn1.pack()
        self.btn2 = Button(root,image=photo,command=self.login)
        self.btn2.pack()
        # 禁用
        # self.btn2.config(state='disable')
    def login(self):
        messagebox.showinfo("QQ","正在登陆")
if __name__ == '__main__':
    root = Tk()
    root.title("QQ")
    root.geometry("500x300+200+300")
    photo = PhotoImage (file='E:/壁纸/4a33ebaf94d00a77e1cddf10b522329f.gif')
    Application(master=root)
    root.mainloop()

