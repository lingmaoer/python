import random

num = random.randint(1,1001)
x=0
while True:
    x+=1
    a = int(input("输入1~1000的数字："))
    if(num==a):
        break
    elif (num>a):
        print("小了")
    else :
        print("大了")
print(x,num)