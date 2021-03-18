import pageage1.module_A as ma

print(ma.a)
# 使用import导入包时，只能跟包名或者模块名

# 使用from导入包时，可以导入包名或者模块名和变量
from pageage1.module_A import a

print(a)
