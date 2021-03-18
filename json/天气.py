import requests
import json
import smtplib
from  email.mime.text import MIMEText

def get_weather():

    url = 'https://free-api.heweather.net/s6/weather/now?1ocation=changsha&key=8a9237lafde5490c9ecf3e9346ff189a'
    #addr_url = url % input("输入你的地点")
    res = requests.get(url).text
    #print(res)
    HeWeather6 = json.loads(res)["HeWeather6"]
    print(HeWeather6)

get_weather()

def smtp_stran(data):
    msg = MIMEText(data,'html','utf-8')
    Host = 'smtp.qq.com'
    Subject = '猪猪'
    From = "205607184@qq.com"
    To = ''

    msg["Subject"] = Subject
    msg['From'] = From
    msg['To'] = To

    server = smtplib.SMTP(Host,25)
    server.set_debuglevel(1)

    server.login(From,)#发起人  邮箱授权码
    server.send(From,[To],msg.as_string())
    server.quit()


