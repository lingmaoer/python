# file = open('a.txt','r')
# print(file.readlines())
# file.close()

# file = open('b.txt','w')
# file.write('Python')
# file.close()

# file = open('b.txt','a')
# file.write('Python')
# file.close()


src_file=open('logo.png','rb')
target_file=open('copylogo.png','wb')
print(target_file.write(src_file.read()))
target_file.close()
src_file.close()