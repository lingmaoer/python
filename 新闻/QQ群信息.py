# -*- encoding: utf-8 -*-
# @Time     :2020/11/9 23:33
# @Author   :lingmao
# @File     :QQ群信息.py
# @Software :PyCharm

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import os
import pandas as pd


def save_data(driver):
    res = driver.page_source  # 获取源码
    driver.quit()  # 关闭浏览器
    soup = BeautifulSoup(res, "lxml")
    html = soup.select("td")

    ## 先用第2、3 个成员判断一下有无 <群标签>字段
    age_2 = html[2 * 10 + 6].text.replace("t", "").replace("n", "")  ## Q龄




