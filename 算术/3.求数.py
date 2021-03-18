'''
题目:一个整数,它加上100后是一一个完全平方数，再加上268又是-一个完全平方数，请问该数是多少?
'''
import math
i=0
while True:
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if x*x==i+100 and y*y==i+268:
        print(i)
        break
    i+=1