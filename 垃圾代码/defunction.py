# !/usr/bin/python3
# --*--coding: utf-8 --*--
# @Time:   2021/3/12 19:12
# @file:   def

# 如果是个数据返回TRUE，不是返回FALSE
def is_num(num):
    try:
        float(num)
        return True
    except ValueError:
        pass


# 求出输入数据的和
def sum_test(num_data):
    sum_num = 0
    for i in num_data:
        sum_num = sum_num + i
    return sum_num
