# -*- encoding: utf-8 -*-
# @Time     :2020/11/10 20:27
# @Author   :lingmao
# @File     :模拟登录.py
# @Software :PyCharm


from selenium import webdriver
import pyautogui
import time

# from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.taobao.com')
    driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
    driver.find_element_by_css_selector('#fm-login-id').send_keys("18272679207")

    driver.find_element_by_css_selector('#fm-login-password').send_keys('xieyuhao123')
    driver.find_element_by_css_selector('#login-form > div.fm-btn > button').click()
    # coords = pyautogui.locateOnScreen('\1.png')
    # x, y = pyautogui.center(coords)
    # pyautogui.leftClick(x, y)

    driver.find_element_by_css_selector('#mc-menu-hd').click()
    driver.find_element_by_css_selector('#J_SelectAll1').click()
    driver.find_element_by_css_selector('#J_FloatBar > div.float-bar-wrapper > div.operations > a.J_DeleteSelected').click()
    driver.find_element_by_css_selector('#ks-stdmod-footer-ks-component457 > a.dialog-btn.J_DialogConfirmBtn').click()
    driver.find_element_by_css_selector("#J_Undo > div > p > a").click()
    driver.find_element_by_css_selector('#J_Item_2287478531738 > ul > li.td.td-op > div > a.J_Del.J_MakePoint').click()
    driver.find_element_by_xpath('//*[@id="ks-stdmod-footer-ks-component449"]/a[1]').click()

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get('https://www.python.org')
#     assert "python" in driver.title
#
#     elem = driver.find_element_by_name('q')
#     elem.send_keys("pycon")
#     elem.send_keys(Keys.RETURN)
#     print(driver.page_source)
