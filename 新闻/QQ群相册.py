# -*- encoding: utf-8 -*-
# @Time     :2020/11/13 20:27
# @Author   :lingmao
# @File     :QQ群相册.py
# @Software :PyCharm

from selenium import webdriver
import time
import pyautogui

group_id = 975377728  # input("输入群号：")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://h5.qzone.qq.com/groupphoto/album?inqq=1&groupId={}'.format(group_id))
# driver.find_elements_by_xpath('#switcher_plogin').click()
time.sleep(3)
# driver.find_element_by_xpath('//*[@id="img_out_2056007184"]').click()

driver.find_element_by_xpath('//*[@id="groupzone_album_list"]/li[1]/div/div[2]/div[1]/a').click()
