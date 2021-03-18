import importlib

#重新导入模块
# importlib.reload()

# 动态导入
a = importlib.import_module("math")


print(a.sin(60))