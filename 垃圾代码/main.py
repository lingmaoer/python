# !/usr/bin/python3
# --*--coding: utf-8 --*--
# @Time:   2021/3/12 18:48
# @file:   main

"""
    题目：
    输入一组数据，求出这组数据的和，输入的数据用空格隔开
    （数据中可能会出现错误，把这些错误的数据去掉）


    算法分析：
    有python输入都是字符串，利用split进行分割得到一个
    数据的列表，再通过循环遍历转化成数据，转化之前先进行
    数据判断是否有输入错误，利用try找出错误，再把求和写成一个函数
    返回数据的和


import defunction

if __name__ == '__main__':
    num_arr_data = []

    # 输入要求和的数据，用空格隔开
    num_arr_str = input("请输入要求和的数：")
    # 利用字符串分割成列表
    num_arr_char = num_arr_str.split()
    # print(num_arr)  # 检查是否切割正确
    for i in num_arr_char:
        if defunction.is_num(i):  # 判断是不是纯数据
            num_arr_data.append(float(i))  # 将字符串转换成数据
        else:
            print(i + "这不是数据")
    # num_sum = sum_test(num_arr_data)

    # 输出数据
    print(str(num_arr_data[0]), end="")
    for i in num_arr_data[1:]:
        print(" + " + str(i), end="")
    print(" = {:.3f}".format(defunction.sum_test(num_arr_data)))  # 输出和,保留三位小数
"""

import math


def str_to_num(num_str):
    num_list = []
    for i in num_str:
        num_list.append(float(i))
    return num_list


def is_triangle(num_list):
    if num_list[0] + num_list[1] > num_list[2] \
            and num_list[1] + num_list[2] > num_list[0] \
            and num_list[2] + num_list[0] > num_list[1]:
        return True


if __name__ == '__main__':
    num_sum = 0
    num_str = input("请输入三角形的三边:")
    num_list_str = num_str.split()
    num_list = str_to_num(num_list_str)
    if is_triangle(num_list):
        for num in num_list:
            num_sum += num
        p = num_sum / 2
        print("三角形面积为", end=" ")
        print("{:.3f}".format(math.sqrt(p * (p - num_list[0]) * (p - num_list[1]) * (p - num_list[2]))))
    else:
        print("这不是一个三角形")
