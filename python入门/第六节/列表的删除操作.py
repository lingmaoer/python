# 一次删除一个，多个只删除第一个

lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
# lst.remove(100)

# pop() 根据索引移除元素
lst.pop(2)
lst.pop()  #删除最后一个元素
print(lst)

print("----------切片操作---------------")
new_lst=lst[1:3]
print("原列表",lst)
print("切片后的列表",new_lst)

# 删除原列表中的内容
lst[1:3]=[]
print(lst)

lst.clear()  # 清空列表
print(lst)

#del 删除列表对象
del lst




