import requests
import pprint
'''
def get_cookie():

    urls = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

    # requests.session(登录信息保持)
    se = requests.session()
    # 请求页面urls
    sea = se.get(urls, headers=headers)
    # 得到页面cookie
    return sea.cookies
    #print (es.cookies)
'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Origin': 'https://www.lagou.com',
    'Host': 'www.lagou.com',
}
def get_cookie():
    urls = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    # requests.session(登录信息保持)
    se = requests.session ()
    # 请求页面urls
    sea = se.get (urls, headers=headers)
    # 得到页面cookie
    #print(sea.cookies)
    return sea.cookies

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
cookie = get_cookie()
data = {
    'first': 'true',
    'pn':'1',
    'kd': 'python'
}
res = requests.post(url,headers = headers,cookies = cookie,data= data).json()
result = res['content']['positionResult']['result']
for i in result:
    #print(i)

    city = i['city']
    district = i['district']
    positionName = i['positionName']
    companyFullName = i['companyFullName']
    salary = i['salary']
    positionAdvantage = i['positionAdvantage']
    workYear = i['workYear']
    #print(city,district,workYear,positionName,companyFullName,salary,positionAdvantage)
    with open('123.csv','a+')as f:
        f.write(city+','+district+','+workYear+','+positionName+','+companyFullName+','+salary+','+positionAdvantage+'\n')


























'''
#requests.session(登录信息保持)
se = requests.session()
#请求页面urls
s = se.get(urls,headers = headers)
#得到页面cookie
cookie = se.cookies
'''






