import traceback

try:
    print("step1")
    num = 1/0
except Exception as result:
    traceback.print_exc()
    #print(result)


try:
    print("step1")
    num = 1/0
except:
    with open('traceback错误处理.txt','w',encoding='utf-8') as f:
        traceback.print_exc(file=f)