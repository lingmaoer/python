'''
题目:输入三个整数x,y,z，请把这三个数由小到大输出。
'''
I=[]
for i in range(3):
    I.append(int(input("输入数%d:"%(i+1))))
I.sort()
print(I)