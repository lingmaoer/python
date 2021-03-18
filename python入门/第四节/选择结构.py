"""
money = 1000  # 余额
s = int(input("请输入取款金额："))
if s <= money:
    money -= s
    print("取款成功，余额为：", money)

num = int(input("请输入一个整数"))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")

score = int(input("请输入一个成绩"))
if 90 <= score <= 100:
    print("A级")
elif 80 <= score < 90:
    print("B级")
elif 70 <= score and score < 80:
    print("C级")
elif 60 <= score and score < 70:
    print("D级")
elif 0 <= score and score < 60:
    print("E级")
else:
    print("成绩有误")

answer = input("您是会员吗？(y/n)")
money = int(input("请输入取款金额："))
if answer == 'y':
    if money >= 200:
        print("应付金额为", money * 0.8)
    elif money >= 100:
        print("应付金额为", money * 0.9)
    else:
        print("应付金额为", money)
else:
    if money >= 200:
        print("应付金额为", money * 0.95)
    else:
        print("应付金额为", money)
"""

# 比较两个整数
num1 = int(input("请输入第一个整数"))
num2 = int(input("请输入第二个整数"))
if num1 >= num2:
    print(num1, "大于等于", num2)
else:
    print(num1, "小于", num2)

print(str(num1)+"大于等于"+str(num2) if num1 >= num2 else str(num1)+"小于"+str(num2))