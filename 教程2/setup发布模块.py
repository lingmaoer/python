# python3 setup.py build

from distutils.core import setup

setup (name="hello_world",  # 包名
       version='1.0',  # 版本号
       description="hello_world",  # 描述信息
       #  long_description="hello_world",  # 详细描述信息
       author="小明",  # 作者
       author_email="xiaoming@QQ.com",  # 邮箱
       url="www.xiaoming.com",  # 主页
       py_modules=["hello_world"]  # 包含模块
       )
# 终端
# 创建源码包
# python3 setup.py sdist


# 上传发布
#进入setup.py文件所在目录
# python setup.py sdist upload

