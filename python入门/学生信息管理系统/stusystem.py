import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择:'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("您确定要退出系统吗？y/n")
                if answer == 'y' or answer == 'Y':
                    print("谢谢您的使用！！！！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('--------------------学生信息管理系统---------------------')
    print('------------------------功能菜单------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')
    print('-------------------------------------------------------')


def insert():
    student_list = []
    while True:
        id = input("请输入id（如1001）：")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            englist = int(input("请输入英语成绩："))
            python = int(input("请输入python成绩："))
            java = int(input("请输入java成绩："))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'english': englist, 'python': python, 'java': java}
        student_list.append(student)
        answer = input("是否继续添加？y/n")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完成：')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input("按ID查找请输入1，按姓名查找请输入2")
            if mode == '1':
                id = input('请输入学生ID')
            elif mode == '2':
                name = input('请输入学生姓名')
            else:
                print("您的输入有误")
                search()
            with open(filename, 'r', encoding='utf-8') as file:
                student = file.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if ['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input("是否继续查询学生信息？y/n")
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print("暂未保存学生信息")
            return


def delete():
    while True:
        student_id = input("请输入要删除的学生的ID：")
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as file:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            file.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag == True:
                        print("id为{}的学生信息已被删除".format(student_id))
                    else:
                        print("没有找到id为{}的学生信息".format(student_id))
            else:
                print("无学生信息")
                break
            show()
            answer = input("是否继续删除？y/n")
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    student_id = input("请输入要修改的学生的ID：")
    with open(filename, 'w', encoding='utf-8')as file:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print("找到学生信息，可以修改他的信息！")
                while True:
                    try:
                        d['name'] = input("请输入姓名：")
                        d['english'] = int(input("请输入英语成绩："))
                        d['python'] = int(input("请输入python成绩："))
                        d['java'] = int(input("请输入java成绩："))
                    except:
                        print("请重新输入")
                    else:
                        break
                file.write(str(d) + '\n')
                print("修改成功！！")
            else:
                file.write(str(d) + '\n')
    answer = input("是否继续修改其他学生信息？y/n")
    if answer == 'y' or answer == 'Y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_list = file.readlines()
        student_new = []
        for i in student_list:
            d = dict(eval(i))
            student_new.append(d)
    else:
        return
    choic = input("请选择你的输入方式：0.升序,1.降序")
    if choic == '0':
        choic_bool = False
    elif choic == '1':
        choic_bool = True
    else:
        print("您的输入有误")
        sort()
    mode = input("请选择排序方式(1.按英语成绩排序2.按Python成绩排序3.按Java成绩排序0.按总成绩排序)")
    if mode == '1':
        student_new.sort(key=lambda student_new: int(student_new['english']), reverse=choic_bool)
    elif mode == '2':
        student_new.sort(key=lambda student_new: int(student_new['python']), reverse=choic_bool)
    elif mode == '3':
        student_new.sort(key=lambda student_new: int(student_new['java']), reverse=choic_bool)
    elif mode == '0':
        student_new.sort(
            key=lambda student_new: int(student_new['english']) + int(student_new['python']) + int(student_new['java']),
            reverse=choic_bool)
    else:
        print("您的输入有误，请重新输入")
        sort()
    show_student(student_new)


def show_student(lst):
    if len(lst) == 0:
        print("没有查询到学生信息，无数据显示！！")
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('id', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for i in lst:
        print(format_data.format(i.get('id'), i.get('name'),
                                 i.get('english'), i.get('python'),
                                 i.get('java'), int(i.get('english')) + int(i.get('python')) + int(i.get('java'), )
                                 ))


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            students = file.readlines()
            if students:
                print("一共有{}名学生".format(len(students)))
            else:
                print('还没有录入学生信息')
    else:
        print("暂未保存数据信息")


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student = file.readlines()
            for i in student:
                student_lst.append(eval(i))
            if student_lst:
                show_student(student_lst)
    else:
        print("暂未保存过数据！！！！")


if __name__ == '__main__':
    main()
