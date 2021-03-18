import random

rand = random.randint(1, 100)
for i in range(1, 11):
    num = int(input("请输入一个数"))
    if rand == num:
        print("答对了")
        break
    elif rand > num:
        print("小了")
        continue
    else:
        print("大了")
        continue
