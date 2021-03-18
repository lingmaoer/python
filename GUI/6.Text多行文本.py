from tkinter import *
import webbrowser

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatwidget()

    def creatwidget(self):
        self.w1=Text(self,width=40,height=12,bg='gray')
        self.w1.pack()

        self.w1.insert(1.0,'0123456789\nabcdefg')
        self.w1.insert(2.4,'获得的的超女吃的v及v给v合肥')

        Button (self,text="重复插入文本", command=self.insertText).pack (side="left")
        Button (self,text="返回文本", command=self.returnText).pack (side="left")
        Button (self,text="添加图片",command=self . addImage) .pack(side="left")
        Button (self,text="添加组件",command=self . addWidget) .pack(side="left")
        Button (self,text="通过tag精确控制文本",command=self.testTag).pack (side="left")

    def insertText(self):
        self.w1.insert(INSERT,'lingmao')
        self.w1.insert(END,'end')
        self.w1.insert(1.8,'hello')

    def returnText(self):
        print(self.w1.get(1.2,1.6))
        print("所有文本内容:\n"+self.w1.get(1.0,END))

    def addImage(self):
        self.photo=PhotoImage(file='E:/壁纸/4a33ebaf94d00a77e1cddf10b522329f.gif')
        self.w1.image_create(END,image = self.photo)

    def addWidget(self):
        self.b1=Button(self.w1,text='xiaolingmao')
        self.w1.window_create(INSERT,window=self.b1)

    def testTag(self):
        self.w1.delete(1.0,END)
        self.w1.insert(INSERT,"good good study,day day up\n345678")
        self.w1.tag_add("good",1.0,1.9)
        self.w1.tag_config("good",background='yellow',foreground='red')

        self.w1.tag_add("baidu",2.0,2.2)
        self.w1.tag_config("baidu",underline=True)
        self.w1.tag_bind("baidu",'<Button-1>',self.webshow)

    def webshow(self,event):
        webbrowser.open("http://www.baidu.com")
if __name__ == '__main__':
    root = Tk()
    root.title("QQ")
    root.geometry("500x300+200+300")
    Application(master=root)
    root.mainloop()
