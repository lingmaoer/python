# -*- encoding: utf-8 -*-
# @Time     :2020/11/14 22:42
# @Author   :lingmao
# @File     :阶乘约数.py
# @Software :PyCharm
"""

【问题描述】
    定义阶乘n! = 1 X 2 X 3 X ...  n。
    请问100! （100 的阶乘）有多少个约数。
【答案提交】
    这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一
    个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
"""
num = 1
primes = []
exp_primes = []
for i in range(2, 101):
    for j in range(2, i + 1):
        if i % j == 0:
            break
    if i == j:
        primes.append(i)

print(primes)
for prime in primes:
    exp = 1
    n = 0
    while prime ** exp <= 100:
        n += 100 // prime ** exp
        exp += 1

    exp_primes.append(n)
print(exp_primes)
num = 1
for i in exp_primes:
    num *= i
print(num)
# 结果：1621986508800
