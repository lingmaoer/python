'''
题目:输入某年某月某日，判断这一天是这一年的第几天?
'''
year=int(input("year:"))
month=int(input("month:"))
day=int(input("day:"))
months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or year%400==0:
    months[2]=29
for i in range(1,month):
    day+=months[i]
print(day)
