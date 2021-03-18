'''
try:
    #程序
except Exception as error:
    print(error)
finally:
'''

'''
URLerror出现的问题：
1.连不上服务器
2.远程url不存在
3.无网络
4.触发HTTPEerror
'''

'''
import urllib.request
import urllib.error
try :
    pass
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)
'''

'''
try:
    #不能确定是否正确的代码
    num = int(input("输入一个整数："))
except:
    #错误提示
    print("请输入正确的整数")
print("-"*50)
'''

'''
try:
    num = int(input("输入一个整数："))
    result = 8/num
    print(result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("请输入正确的数")
'''

'''
try:
    num = int(input("输入一个整数："))
    result = 8/num
    print(result)
except ValueError:
    print("请输入正确的数")
except Exception as result:
    print(f"未知错误  {result}")
'''

'''
try:
    num = int(input("输入一个整数："))
    result = 8/num
    print(result)
except ValueError:
    print("请输入正确的数")
except Exception as result:
    print(f"未知错误  {result}")
else:
    print("尝试成功")
finally:
    print("无论成功与否都执行")
'''

#异常传递
'''
def demo1():
    return int(input("输入整数:"))

def demo2():
    return demo1()

try :
    print(demo2())
except Exception as result:
    print(result)
'''


#主动给出异常
def input_password():
    pwd = input("输入密码：")
    if len(pwd)>=8:
        return
    print("主动抛出异常")
    #创建异常
    ex = Exception("密码长度不够")

    raise ex
try:
    print(input_password())
except Exception as result:
    print(result)






