DaysPerYear = input ("请输入年份：")
HoursPerDay = 24
MinutesperHours = 60
SecondsPerMinute = 60
if eval(DaysPerYear)%4==0 and eval(DaysPerYear)%100!=0 or eval(DaysPerYear)%400==0:
    print(366 * HoursPerDay * MinutesperHours * SecondsPerMinute)
else:
    print(365 * HoursPerDay * MinutesperHours * SecondsPerMinute)