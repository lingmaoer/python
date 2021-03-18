import os

# path = os.getcwd()
# lst = os.listdir(path)
# for filename in lst:
#     if filename.endswith('.py'):
#         print(filename)

path = os.getcwd()
lst = os.walk(path)
for dirpath,dirname,filename in lst:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('-'*50)
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    print('-'*50)