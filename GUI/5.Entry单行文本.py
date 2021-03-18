from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatwidget()

    def creatwidget(self):
        self.label = Label(self,text='用户名')
        self.label.pack()

        # StringVar变量绑定到指定的组件
        # StringVar变量的值发生变化，组件内容也发生变化
        # 组件内容发生变化，StringVar变量的值也发生变化。
        v1 = StringVar()
        self.entry1=Entry(self,text=v1)
        self.entry1.pack()
        v1.set("admin")
        # print(v1.get(),self.entry1.get())

        self.labe2 = Label(self,text='密码')
        self.labe2.pack()
        v2 = StringVar()
        self.entry2=Entry(self,text=v2,show='*')
        self.entry2.pack()
        v2.set("password")

        Button(self,text='登录',command=self.login).pack()

    def login(self):
        username=self.entry1.get()
        password=self.entry2.get()
        # print(username,password)
        if username=="123456" and password=='123456':
            messagebox.showinfo("QQ","登陆成功")
        else:
            messagebox.showinfo ("QQ", "登陆失败")
if __name__ == '__main__':
    root = Tk()
    root.title("QQ")
    root.geometry("500x300+200+300")
    # photo = PhotoImage (file='E:/壁纸/4a33ebaf94d00a77e1cddf10b522329f.gif')
    Application(master=root)
    root.mainloop()
