for i in range(3):
    pwd = input("请输入密码：")
    if pwd == '8888':
        print("输入正确：")
        break
    else:
        print("密码不正确")

a = 0
while a < 3:
    pwd = input("请输入密码：")
    if pwd == '8888':
        print("输入正确：")
        break
    else:
        print("密码不正确")
    a += 1
