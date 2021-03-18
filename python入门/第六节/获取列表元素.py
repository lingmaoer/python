# 单个元素
lst = ['hello', 'world', 98, 'hello', 'world', 234]

print(lst[2])
print(lst[-3])

# 多个元素
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print("原列表", id(list))
lst2 = lst[1:6:1]
print("新列表", id(lst2))
print(lst[1:6])
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])
print(lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2])
