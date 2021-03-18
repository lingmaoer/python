from distutils.core import setup

setup (name="hello_world",  # 包名
       version='1.0',  # 版本
       description="hello_world",  # 描述信息
       long_description="hello_world",  # 详细描述信息
       author="小明",  # 作者
       author_email="xiaoming@QQ.com",  # 邮箱
       url="www.xiaoming.com",  # 主页
       py_modules=["hello_world"]  # 包含模块
       )
# 终端
# python3 setup.py build
# python3 setup.py sdist


