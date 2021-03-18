from tkinter import *
import random

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatwidget()

    def creatwidget(self):
        self.canvas=Canvas(self,width=300,height=200,bg='green')
        self.canvas.pack()

        #画一条直线
        line=self.canvas.create_line(10,10,30,20,40,50)
        #画一个矩形
        rect=self.canvas.create_rectangle(50,50,100,100)
        #画一个椭圆
        oval=self.canvas.create_oval(50,50,100,100)

        #self.canvas.create_image(150,170,image=photo)

        Button(self,text='画矩形',command=self.draw).pack(side='left')

    def draw(self):
        for i in range(0,10):
            x1= random.randrange(int(self.canvas['width'])/2)
            y1 = random.randrange (int (self.canvas['height'] )/ 2)
            x2=x1 + random.randrange(int(self.canvas['width'])/2)
            y2 =y1 + random.randrange (int (self.canvas['height'] )/ 2)
            self.canvas.create_rectangle(x1,y1,x2,y2)


if __name__ == '__main__':
    root = Tk()
    root.title("QQ")
    root.geometry("500x300+200+300")
    # photo = PhotoImage (file='E:/壁纸/4a33ebaf94d00a77e1cddf10b522329f.gif')
    Application(master=root)
    root.mainloop()