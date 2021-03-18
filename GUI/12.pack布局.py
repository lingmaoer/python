from tkinter import *

root=Tk()
root.geometry("700x220+300+300")
f1=Frame(root).pack()
f2=Frame(root).pack()
btntext=("轻音乐","重金属","日本风","中国风","流行风")
for btn in btntext:
    Button(root,text=btn).pack(side='left',padx=10)
for i in range(1,13):
    Label(f2,width=5,height=10,borderwidth=1,relief='solid',bg='black' if i%2==0 else 'white').pack(side="left",padx=2)

root.mainloop()