from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatwidget()

    def creatwidget(self):
        self.label1=Label(self,text="用户名")
        self.label1.grid(row=0,column=0)

        self.entry1=Entry(self)
        self.entry1.grid(row=0,column=1)

        Label(self,text="(用户名为手机号)").grid(row=0,column=2)

        Label(self,text='密码',).grid(row=1,column=0)
        Entry (self).grid(row=1,column=1)

        Button(self,text='登录').grid(row=2,column=1,sticky=EW)
        Button (self,text='取消').grid (row=2, column=2, sticky=E)

if __name__ == '__main__':
    root = Tk()
    root.title("QQ")
    root.geometry("500x300+200+300")
    Application(master=root)
    root.mainloop()

# columspan  跨越的列数
# rowspan  跨越的行数
# ipadx 子组件距离x方向
# ipady 子组件距离y方向
# padx 组件距离x方向
# pady 组件距离y方向
# sticky 组件紧贴所在的单元格