import os

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

print(factorial(5))


def Getallfile(path):
    childfile = os.listdir(path)
    for file in childfile:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            Getallfile(filepath)
        print(os.path.join(path,file))


Getallfile(r'E:\biancheng\python')