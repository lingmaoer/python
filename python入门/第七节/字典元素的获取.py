scores = {'张三': 100, '李四': 98, '王五': 45}

print(scores['张三'])
# print(scores['陈六'])


print(scores.get("张三"))
print(scores.get("陈六"))
print(scores.get("麻七", 99))
