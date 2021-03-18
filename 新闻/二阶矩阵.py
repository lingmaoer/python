# -*- encoding: utf-8 -*-
# @Time     :2020/11/11 13:46
# @Author   :lingmao
# @File     :二阶矩阵.py
# @Software :PyCharm
z = 0
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        for g in range(0, 10):
                            for h in range(0, 10):
                                if (a * e + b * g == a * 10 + e) and (c * e + d * g == c * 10 + g) and (
                                        a * f + b * h == b * 10 + f) and (c * f + d * h == d * 10 + h):
                                    print(a, '\t', b, '\t', e, '\t', f, '\t', a * e + b * g, '\t', a * f + b * h)
                                    print(c, '\t', d, '\t', g, '\t', h, '\t', c * e + d * g, '\t', c * f + d * h)
                                    z += 1
                                    print()
print(z)
