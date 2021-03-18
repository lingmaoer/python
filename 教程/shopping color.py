menu = [
    ('Iphone',5800),
    ('Mac pro',9800),
    ('Bike',800),
    ('coffe',31),
    ('book',100),
    ('Match',8000)
]
money = int(input("\033[36:1m your money:\033[0m"))
shopping_cart = []
count = []
judjement = True
while judjement:
    print('\033[35:1m if you want quit,please imput \'q\'\033[0m')
    for index,i in enumerate(menu):
        print('\033[31:1m %d  %s\033[0m'%(index+1,i))
    quit = input ('Do you want to going shopping (please answer y or n)')
    if quit=='y' or quit == 'Y':
        user_choice1 = int(input("\033[33:1m Please select the serial number before the goods:\033[0m"))
        user_choice2 = int(input("\033[34:1m Please enter the number you want to buy:\033[0m"))
        if menu[user_choice1-1][1]*user_choice2 <= money:
            money -= menu[user_choice1-1][1]*user_choice2
            shopping_cart.append(menu[user_choice1-1])
            count.append(user_choice2)
            print('\033[32:1m Your money is surplus %d,your shopping cart have %s\033[0m'%(money,list(zip(count,shopping_cart))))
        else:
            print("\033[33:1m Your balance is insufficient, rush to make money\033[0m")
    else:
        break
for indx,i in enumerate(count):
    print("\033[44:1m %d个%s花费%d\033[0m"%(i,shopping_cart[indx][0],i*shopping_cart[indx][1]))
print("你还有%d"%(money))

