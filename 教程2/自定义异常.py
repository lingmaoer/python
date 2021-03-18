
def input_password():

    pwd = input("输入密码：")
    if len(pwd)>=8:
        return
    print("主动抛出异常")
    # 创建异常
    ex = Exception("密码长度不够")

    raise ex
try:
    print(input_password())
except Exception as result:
    print(result)


