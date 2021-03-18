account = 'abcdefg'
password = '1234567'

count = 0
while count<3:

    user_account = input()
    user_passeord = input()
    if account == user_account and password ==user_passeord:
        print('success')
        break
    else :
        print("fail")
    count += 1
    if count ==3:
        print('you account is blocked')
        break
