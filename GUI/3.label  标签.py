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
        self.label1 = Label(self,text='猪头',width=8,height=2,fg='white',bg='black')
        self.label1.config(fg='red',bg='green')
        self.label1.pack()
        self.label2 = Label(self,text='臭猪头',width=8,height=2,fg='blue',bg='black',font=("黑体",30))
        self.label2.pack()
        # 显示图像
        # photo = PhotoImage(file='E:/壁纸/4a33ebaf94d00a77e1cddf10b522329f.gif')
        #self.label3 = Label(self,image=photo)
        #self.label3.pack()
        self.label4 = Label(self,text='小绿\n小明\n小红\n',borderwidth=5,relief='groove',justify='right')#solid
        self.label4.pack()
if __name__ == '__main__':

    root = Tk()
    root.geometry("1000x600+150+100")
    root.title('一个经典GUI的类的写法')
    #photo = PhotoImage (file='E:/壁纸/4a33ebaf94d00a77e1cddf10b522329f.gif')
    app = Application(master = root)

    root.mainloop()