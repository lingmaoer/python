from tkinter import *


class Application(Frame):
    v1 = StringVar ()
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatwidget()

    def creatwidget(self):

        Entry(self,text=self.v1).grid(row=0,column=0,columnspan=4,pady=10)

        Button(self,text="MC",width=2).grid(row=1,column=0,sticky=EW)
        Button(self,text="M+",width=2).grid(row=1,column=1,sticky=EW)
        Button(self,text="M-",width=2).grid(row=1,column=2,sticky=EW)
        Button(self,text="MR",width=2).grid(row=1,column=3,sticky=EW)
        Button(self,text="C",width=2).grid(row=2,column=0,sticky=EW)
        Button(self,text="±",width=2).grid(row=2,column=1,sticky=EW)
        Button(self,text="/",width=2).grid(row=2,column=2,sticky=EW)
        Button(self,text="×",width=2).grid(row=2,column=3,sticky=EW)
        Button(self,text=7,width=2,command=self.num7).grid(row=3,column=0,sticky=EW)
        Button(self,text=8,width=2,).grid(row=3,column=1,sticky=EW)
        Button(self,text=9,width=2).grid(row=3,column=2,sticky=EW)
        Button(self,text="-",width=2).grid(row=3,column=3,sticky=EW)
        Button(self,text=4,width=2).grid(row=4,column=0,sticky=EW)
        Button(self,text=5,width=2).grid(row=4,column=1,sticky=EW)
        Button(self,text=6,width=2).grid(row=4,column=2,sticky=EW)
        Button(self,text="+",width=2).grid(row=4,column=3,sticky=EW)
        Button(self,text=1,width=2).grid(row=5,column=0,sticky=EW)
        Button(self,text=2,width=2).grid(row=5,column=1,sticky=EW)
        Button(self,text=3,width=2).grid(row=5,column=2,sticky=EW)
        Button(self,text="=",width=2).grid(row=5,column=3,sticky=NSEW,rowspan=2)
        Button(self,text=0,width=2).grid(row=6,column=0,sticky=EW,columnspan=2)
        Button(self,text=".",width=2).grid(row=6,column=2,sticky=EW)
    def num7(self):
        self.v1.trace_add(7)

if __name__ == '__main__':
    root = Tk()
    root.title("计算器")
    root.geometry("250x250+200+300")

    Application(master=root)
    root.mainloop()