from selenium import webdriver
import time
import csv

def search_product(key):
    driver.find_element_by_id("q").send_keys(key)
    driver.find_element_by_class_name("btn-search").click()
    driver.maximize_window()
    time.sleep(15)

def get_product():
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        info = div.find_element_by_xpath(".//div[@class='row row-2 title']/a").text
        price = div.find_element_by_xpath(".//strong").text+"元"
        deal = div.find_element_by_xpath (".//div[@class='deal-cnt']").text + "人"
        name = div.find_element_by_xpath (".//div[@class='shop']").text

        print(info,price,deal,name,sep="|")
        with open("data.csv",'a',newline='')as f:
            csvwriter = csv.writer(f,delimiter=',')
            csvwriter.writerow([info,price,deal,name])
def main():
    search_product(keyword)
    get_product()
if __name__ == '__main__':

    keyword = input()
    driver = webdriver.Chrome()
    driver.get("https://www.taobao.com")
    main()

