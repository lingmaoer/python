import sys
from you_get import common as you_get  # 导入you-get库

"""urls = ["https://www.bilibili.com/bangumi/play/ep232465",
        "https://www.bilibili.com/bangumi/play/ep232466",
        "https://www.bilibili.com/bangumi/play/ep232467",
        "https://www.bilibili.com/bangumi/play/ep232468",
        "https://www.bilibili.com/bangumi/play/ep232469",
        "https://www.bilibili.com/bangumi/play/ep232470",
        "https://www.bilibili.com/bangumi/play/ep232471",
        "https://www.bilibili.com/bangumi/play/ep232472",
        "https://www.bilibili.com/bangumi/play/ep232473",
        "https://www.bilibili.com/bangumi/play/ep232474",
        "https://www.bilibili.com/bangumi/play/ep232475",
        "https://www.bilibili.com/bangumi/play/ep232476",
        "https://www.bilibili.com/bangumi/play/ep249937",
        "https://www.bilibili.com/bangumi/play/ep258941"
        ]"""
directory = r'D:'  # 设置下载目录


def fun(url):
    # url = f"https://www.bilibili.com/bangumi/play/ep2850{i}" # 需要下载的视频地址
    sys.argv = ['you-get', '--playlist', '-o', directory, url]  # sys传递参数执行下载，就像在命令行一样
    you_get.main()


if __name__ == '__main__':
    # url = "https://www.bilibili.com/video/BV1wT4y1G7UQ"
    url ="https://www.bilibili.com/video/BV1wT4y1G7UQ?from=search&seid=10609415456249474590"
    fun(url)

