# 一.使用print方式进行输出（输出的目地地是文件）
# fp = open('test.txt', 'w')
# print("奋斗成就更好的你", file=fp)
# fp.close()

with open('test.txt', 'w') as file:
    file.write("奋斗成就更好的你1!!")

