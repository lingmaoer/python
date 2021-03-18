#记录年份，判断生肖
Chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊' 
#print (Chinese_zodiac[0:4])   输出：鼠牛虎兔
#print (Chinese_zodiac[-1])    输出；猪
year = 2020

print (Chinese_zodiac[year%12])

print ('狗' in Chinese_zodiac)

print ('狗' not in Chinese_zodiac)

print (Chinese_zodiac + Chinese_zodiac)

print (Chinese_zodiac * 4)
