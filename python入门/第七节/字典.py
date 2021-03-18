# 无序
# 可变   KEY不可变对象，不允许重复
# values 可以重复
# 键值对存储

scores = {'张三': 100, '李四': 98, "王五": 45}
print(scores)
print([type(scores)])

student = dict(name='jack', age=20)
print(student)

# 空字典
d = {}
print(d)

a = {'name': '张三', 'name': '李四'}
print(a)

a = {'name': '张三', 'nikename': '李四'}
print(d)

lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)
