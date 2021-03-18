import time
import calendar

a=time.time()#1970.1.1  秒
b=time.asctime()
print(a)
print(b)
for c in range(1,10,2):
    print(c)
    time.sleep(0.5)
print(time.localtime())

print("2020是否闰年：",calendar.isleap(2020))
print(calendar.month(2020,3))
print(calendar.calendar(2020))
