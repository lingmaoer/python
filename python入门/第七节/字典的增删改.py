scores = {"张三": 100, "李四": 98, "王五": 45}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']  # 删除字典的元素
# scores.clear()     # 清空字典的元素
print(scores)
scores['陈六'] = 98   # 增加元素
print(scores)

scores['陈六'] = 100  # 修改元素
print(scores)
