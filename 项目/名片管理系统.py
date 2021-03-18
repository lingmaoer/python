#所有名片
all_card = []
#系统首页
def home_page():
    print('*' * 60)
    print('欢迎使用【名片管理系统】 v1.0'+'\n')
    print("1.新建名片")
    print("2.显示全部名片")
    print("3.查询名片"+'\n')
    print ("0.退出系统")
    print ('*' * 60)

#新建名片
def new_card():

    card = {}
    name = input("输入姓名：")
    card['name'] = name
    telephone = input("输入电话：")
    card['telephone'] = telephone
    QQ = input("输入QQ：")
    card['QQ'] = QQ
    email = input("输入邮件：")
    card['email'] = email
    all_card.append(card)
    print(f"成功添加 {card['name']} 的名片")

#修改名片
def change_card(card):
    name = input ("输入姓名[回车不修改]:")
    if name != '':
        card['name'] = name
    telephone = input ("输入电话[回车不修改]:")
    if telephone != '':
        card['telephone'] = telephone
    QQ = input ("输入QQ[回车不修改]:")
    if QQ != '':
        card['QQ'] = QQ
    email = input ("输入邮件[回车不修改]:")
    if email != '':
        card['email'] = email
    print(f"成功修改 {card['name']} 的名片")

while True:
    home_page()
    num = int(input("请选择操作功能:"))
    print("您选择的操作是:{}".format(num))
    print ("-" * 60)
    if num==1:
        print ("功能：新建名片")
        new_card()
    elif num==2:
        print ("功能：显示全部名片")
        if len (all_card) == 0:
            print("提示：没有任何名片记录")
        else:
            for i in all_card:
                print("{:5}{:15}{:15}{:20}".format('名字','电话','QQ','邮箱'))
                print ("-" * 60)
                print('{:5}{:15}{:15}{:20}'.format(i['name'],i['telephone'],i['QQ'],i['email']))
    elif num==3:
        print ("功能：查询名片")
        name = input('请输入要查询的名字：')
        for i in all_card:
            if i['name'] == name:
                print("{:5}{:15}{:15}{:20}".format('名字','电话','QQ','邮箱'))
                print ("-" * 60)
                print('{:6}{:15}{:15}{:20}'.format(i['name'],i['telephone'],i['QQ'],i['email']))
                num1 = int(input("输入对名片的操作：1.修改 / 2.删除 / 0.返回上级菜单："))
                if num1==1:
                    change_card(i)
                elif num1==2:
                    all_card.remove(i)
                    print("提示：删除成功")
                elif num1==0:
                    break
    elif num==0:
        print ("欢迎再次使用【名片管理系统】")
        break
    else :
        print("提示：非法操作！")
        continue