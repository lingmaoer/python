from tkinter import *

root=Tk()
root.geometry("200x100")

v=StringVar(root)
v.set("aaaa")
om=OptionMenu(root,v,"1111",'4444','6666')

om['width']=10
om.pack()

def test1():
    print("play game:",v.get())

Button(root,text='确定',command=test1).pack()
root.mainloop()