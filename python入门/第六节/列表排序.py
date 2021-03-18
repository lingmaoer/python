lst = [20, 40, 10, 87, 54]
print("排序前", lst, id(list))

lst.sort()
print("排序后", lst, id(list))

lst.sort(reverse=True)
print("排序后", lst, id(list))

print('-----使用内置函数sorted()对列表进行排序，将产生一个新的列表-------')
lst = [20, 40, 10, 87, 54]
print("排序前", lst, id(list))
new_lst = sorted(lst)
print(lst)
print(new_lst)

new_lst = sorted(lst, reverse=True)
print(lst)
print(new_lst)
