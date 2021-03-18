'''import sys
print(sys.getdefaultencoding())
s = "你好"
s_to_unicode = s.decode("utf-8")
s_to_gbk = s_to_unicode.encode("gbk")
print(s_to_unicode)'''

'''
import time
p=int(input())
fun=2
n=1
start = time.time()
while True:
    n+=1
    fun*=n
    if(fun%p==0):
        print(fun)
        break
over = time.time()
print(over-start)
'''
'''
a = eval(input("输入a:"))
b = eval(input("输入b:"))

def min(a , b) :
    if a > b :
        m = b
    else :
        m = a
    while True :
        if(a % m == 0 and b % m == 0):
            break
        else :
            m -= 1
    return m

def max(a , b) :
    if a > b :
        m = a
    else :
        m = b
    while True :
        if(m % a == 0 and m % b == 0):
            break
        else :
            m += 1
    return m

min = min(a,b)
max = max(a,b)

print(f'min = {min},max = {max}')

'''
from PIL import Image,ImageTk
from tkinter import *

data = ['猪','猫','狗','熊']
#  记录当前状态
#  正在运行
going = True
#  滚动状态
is_run = False
# TK创建窗口
window = Tk()
# 设置尺寸  (250  15)初始定位
window.geometry('400x320+250+15')
#标题
window.title("抽奖")
# 读取背景图  绝对路径，相对路径
image = Image.open("6666.jpg")
#转换
photo = ImageTk.PhotoImage(image)
#放置背景
var1 = StringVar(value='即将开始')
show_labell = Label(window, textvariable=var1,width = 360, height =100, bg= '#A8A8A8',font='楷体 -40 bold', foregrount = 'pink',image=photo,compound=CENTER)

show_labell.place(x=20,y=20)

var2 = StringVar(value='幸运儿是你吗？')
show_labell = Label(window, textvariable=var2,width = 38, height =3, bg= '#A8A8A8',font='楷体 -18 bold', foregrount = 'red')

show_labell.place(x=20,y=240)

button1 =Button(window, text='开始',width = 14, height =2, bg='#BFEFF',font='宋体 -18 bold', command = lambda : start(var1,var2))
show_labell.place(x=20,y=175)

button2 =Button(window, text='结束',width = 14, height =2, bg='#BFEFF',font='宋体 -18 bold', command = lambda : end(var1,var2))
show_labell.place(x=232,y=175)

#运行
window.mainloop()

























