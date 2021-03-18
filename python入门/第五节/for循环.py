"""
for item in "python":
    print(item)
"""

for i in range(10):
    print(i)

# 如果循环体不需要使用到自定义变量，可将自定义变量写为_
for _ in range(5):
    print("人生苦短,我用Python")

sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)
