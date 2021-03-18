from http.cookiejar import CookieJar
from urllib import request
from urllib import parse

#创建一个CookieJar对象
cookiejar = CookieJar()

handler = request.HTTPCookieProcessor(cookiejar)

opener = request.build_opener(handler)

headers = {}

data = {
    'email':'',
    'password':''
}

login_url = ''

req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)


