lst = [10, 20, 30]
print(lst, id(lst))
lst.append(100)  # 结尾追加一条数据
print(lst, id(lst))
lst2 = ['hello', 'world']
# lst.append(lst2)   # 将list2作为一个元素，添加到链表的末尾
print(lst, id(lst))
lst.extend(lst2)  # 向列表末尾添加多个元素
lst.insert(2, 10)  # 向链表任意位置 添加一个元素
print(lst, id(lst))

# 在列表任意一个位置添加至少一个数据
lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)
