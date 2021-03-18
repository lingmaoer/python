# file = open('a.txt', 'r')
# print(file.read(2))
# print(file.readline())
# print(file.readlines())
# file.close()

# file = open('c.txt', 'a')
# # file.write('hello')
# lst = ['java', 'go', 'python', 'C/C++']
# file.writelines(lst)
# file.close()

# file=open("a.txt",'r')
# # file.seek(1)  中文占两个字节
# file.seek(2)
# print(file.read())
# print(file.tell())
# file.close()

file=open('d.txt','a')
file.write('hello\n')
file.flush()
file.write('world')
file.close()
