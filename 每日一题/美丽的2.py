# -*- encoding: utf-8 -*-
# @Time     :2020/11/14 14:30
# @Author   :lingmao
# @File     :美丽的2.py
# @Software :PyCharm

"""
【问题描述】
    小蓝特别喜欢2，今年是公元2020 年，他特别高兴。
    他很好奇，在公元1 年到公元2020 年（包含）中，有多少个年份的数位中
    包含数字2？
【答案提交】
    这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一
    个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
    试
"""

num = 0
for i in range(1, 2021):
    if i < 10:
        if i % 10 == 2:
            num += 1
            # print(i)
    elif 10 <= i < 100:
        if i // 10 == 2 or i % 10 == 2:
            num += 1
            # print(i)
    elif 100 <= i < 1000:
        if i // 100 == 2 or i // 10 % 10 == 2 or i % 10 == 2:
            num += 1
            # print(i)
    else:
        if i // 1000 == 2 or i // 100 % 10 == 2 or i // 10 % 10 == 2 or i % 10 == 2:
            num += 1
            # print(i)

print(num)
# 结果：563
