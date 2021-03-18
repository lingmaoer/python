'''
一段代码
'''

ACCOUND = '123456'
password = '123456'

print('please input ACCOUND')
user_ACCOUND =input()

print('please input password')
user_password = input()
if ACCOUND == user_ACCOUND and password == user_password:
        print('success')
else:
        print('fail')