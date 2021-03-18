from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatwidget()

    def creatwidget(self):
        self.codehabby=IntVar()
        self.videoHobby=IntVar()

        self.c1=Checkbutton(self,text='敲代码',variable=self.codehabby,onvalue=1,offvalue=0)
        self.c2=Checkbutton(self,text='看电视',variable=self.videoHobby,onvalue=1,offvalue=0)

        self.c1.pack(side='left')
        self.c2.pack (side='left')

        Button(self,text='确定',command=self.confirm).pack(side='left')

    def confirm(self):
        if self.videoHobby.get()==1:
            messagebox.showinfo("测试","看视频")
        if self.codehabby.get()==1:
            messagebox.showinfo("测试","滚去学习")
if __name__ == '__main__':
    root = Tk()
    root.title("QQ")
    root.geometry("500x300+200+300")
    Application(master=root)
    root.mainloop()