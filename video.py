# !/usr/bin/python3
# --*--coding: utf-8 --*--
# @Time:   2021/3/17 11:15
# @file:   video
# @Author: yuhao Xie


import sys
import ffmpeg

directory = r'D:\PID'  # 设置下载目录

if __name__ == '__main__':
    for i in range(1, 8):
        sys.argv = ["ffmpeg", "-i", "{}.flv".format(i), "{}.mp4".format(i)]
