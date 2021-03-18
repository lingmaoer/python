# -*- encoding: utf-8 -*-
# @Time     :2020/11/3 0:47
# @Author   :ling_mao
# @File     :photo.py
# @Software :PyCharm

import requests
import json

name_list = []
base_url = ["https://h5.qzone.qq.com/proxy/domain/u.photo.qzone.qq.com/cgi-bin/upp/qun_floatview_photo?g_tk=42216759&qzonetoken=6a33923d7770a74012837fc235b0ba9135b8734334fb2812cbc969c081ef7370c58443691e1397e5f22e45ec4192933d6ea6ea&callback=viewer_Callback&t=318114303&topicId=975377728_JyMEfN1*si4KS4ODkiDYww!!&picKey=V5bCQA5NzUzNzc3MjhNW69ftueLKQ!!&shootTime=&cmtOrder=1&fupdate=1&plat=qzone&source=qzone&cmtNum=10&likeNum=5&inCharset=utf-8&outCharset=utf-8&callbackFun=viewer&offset=0&number=20&uin=2056007184&hostUin=2056007184&appid=421&isFirst=1&sortOrder=3&showMode=1&prevNum=9&postNum=18&_=1605617304820",
            "https://h5.qzone.qq.com/proxy/domain/u.photo.qzone.qq.com/cgi-bin/upp/qun_floatview_photo?g_tk=42216759&qzonetoken=6a33923d7770a74012837fc235b0ba9135b8734334fb2812cbc969c081ef7370c58443691e1397e5f22e45ec4192933d6ea6ea&callback=viewer_Callback&t=638951427&topicId=975377728_JyMEfN1*si4KS4ODkiDYww!!&picKey=V5bCQA5NzUzNzc3Mjh8LqpfA1ZsIA!!&shootTime=&cmtOrder=1&fupdate=1&plat=qzone&source=qzone&cmtNum=10&likeNum=5&inCharset=utf-8&outCharset=utf-8&callbackFun=viewer&offset=19&number=20&uin=2056007184&hostUin=2056007184&appid=421&isFirst=&sortOrder=3&showMode=1&prevNum=0&postNum=20&_=1605617304823",
            "https://h5.qzone.qq.com/proxy/domain/u.photo.qzone.qq.com/cgi-bin/upp/qun_floatview_photo?g_tk=42216759&qzonetoken=a44598d02ccf0f26c2d9e69ac3fb8071d605d2a7dd4a0bc4bcc790e2d5c0137c5835c10549c371fa7500f6e6aaeb4dfcd1d90c&callback=viewer_Callback&t=841179041&topicId=975377728_V502xGIH2p1jLC3hkZlX0ZP5tF1DqriB&picKey=V5bCQA5NzUzNzc3MjjlXK9f7J.BBw!!&shootTime=&cmtOrder=1&fupdate=1&plat=qzone&source=qzone&cmtNum=10&likeNum=5&inCharset=utf-8&outCharset=utf-8&callbackFun=viewer&offset=0&number=20&uin=2056007184&hostUin=2056007184&appid=421&isFirst=1&sortOrder=3&showMode=1&prevNum=9&postNum=18&_=1605617510701",
            "https://h5.qzone.qq.com/proxy/domain/u.photo.qzone.qq.com/cgi-bin/upp/qun_floatview_photo?g_tk=42216759&qzonetoken=a44598d02ccf0f26c2d9e69ac3fb8071d605d2a7dd4a0bc4bcc790e2d5c0137c5835c10549c371fa7500f6e6aaeb4dfcd1d90c&callback=viewer_Callback&t=994390332&topicId=975377728_V502xGIH2p1jLC3hkZlX0ZP5tF1DqriB&picKey=V5bCQA5NzUzNzc3Mjjpfatf5QK3GA!!&shootTime=&cmtOrder=1&fupdate=1&plat=qzone&source=qzone&cmtNum=10&likeNum=5&inCharset=utf-8&outCharset=utf-8&callbackFun=viewer&offset=19&number=20&uin=2056007184&hostUin=2056007184&appid=421&isFirst=&sortOrder=3&showMode=1&prevNum=0&postNum=20&_=1605617510705",
            "https://h5.qzone.qq.com/proxy/domain/u.photo.qzone.qq.com/cgi-bin/upp/qun_floatview_photo?g_tk=42216759&qzonetoken=a44598d02ccf0f26c2d9e69ac3fb8071d605d2a7dd4a0bc4bcc790e2d5c0137c5835c10549c371fa7500f6e6aaeb4dfcd1d90c&callback=viewer_Callback&t=461953100&topicId=975377728_V502xGIH2p1jLC3hkZlX0ZP5tF1DqriB&picKey=V5bCQA5NzUzNzc3Mji0fqpf*FLuBA!!&shootTime=&cmtOrder=1&fupdate=1&plat=qzone&source=qzone&cmtNum=10&likeNum=5&inCharset=utf-8&outCharset=utf-8&callbackFun=viewer&offset=39&number=20&uin=2056007184&hostUin=2056007184&appid=421&isFirst=&sortOrder=3&showMode=1&prevNum=0&postNum=20&_=1605617510706",
            "https://h5.qzone.qq.com/proxy/domain/u.photo.qzone.qq.com/cgi-bin/upp/qun_floatview_photo?g_tk=42216759&qzonetoken=a44598d02ccf0f26c2d9e69ac3fb8071d605d2a7dd4a0bc4bcc790e2d5c0137c5835c10549c371fa7500f6e6aaeb4dfcd1d90c&callback=viewer_Callback&t=568663156&topicId=975377728_V502xGIH2p1jLC3hkZlX0ZP5tF1DqriB&picKey=V5bCQA5NzUzNzc3MjhdS6pfs*7jNw!!&shootTime=&cmtOrder=1&fupdate=1&plat=qzone&source=qzone&cmtNum=10&likeNum=5&inCharset=utf-8&outCharset=utf-8&callbackFun=viewer&offset=59&number=20&uin=2056007184&hostUin=2056007184&appid=421&isFirst=&sortOrder=3&showMode=1&prevNum=0&postNum=20&_=1605617510707",
            "https://h5.qzone.qq.com/proxy/domain/u.photo.qzone.qq.com/cgi-bin/upp/qun_floatview_photo?g_tk=42216759&qzonetoken=a44598d02ccf0f26c2d9e69ac3fb8071d605d2a7dd4a0bc4bcc790e2d5c0137c5835c10549c371fa7500f6e6aaeb4dfcd1d90c&callback=viewer_Callback&t=848091280&topicId=975377728_V502xGIH2p1jLC3hkZlX0ZP5tF1DqriB&picKey=V5bCQA5NzUzNzc3MjipG6pf0GtwKw!!&shootTime=&cmtOrder=1&fupdate=1&plat=qzone&source=qzone&cmtNum=10&likeNum=5&inCharset=utf-8&outCharset=utf-8&callbackFun=viewer&offset=79&number=20&uin=2056007184&hostUin=2056007184&appid=421&isFirst=&sortOrder=3&showMode=1&prevNum=0&postNum=20&_=1605617510708",
            ]
cookie = 'RK=SsD08ttHFs; ptcz=d8cfc4284c7eca1fb210695cd0ebdc5b4c90d8641ba71041b581a6997606453a; pgv_pvi=3387736064; pgv_pvid=3964851136; QZ_FE_WEBP_SUPPORT=1; cpu_performance=2; __Q_w_s_hat_seed=1; iip=0; luin=o2056007184; eas_sid=y1V6Q044Q548R1u5i0t9b6i0P9; lskey=00010000fba11a31dcc1525322cceddcb4974e0997ca37acdbdd9c8a104a8edaa03957fdfb2b435b561fbd0e; o_cookie=2056007184; pac_uid=1_2056007184; cpu_performance_v8=7; uin=o2056007184; skey=@MuhW84FnW; p_uin=o2056007184; pt4_token=6HSaTiwjoil3xYndWfWfsxoNBCSUXPFzP0hrHdHnbOQ_; p_skey=W-QwCMuSYzX0sfF1AAb8ucsA1I5FIMF0f39l66wlR5g_; pgv_info=ssid=s6669457460; rv2=805181A445E8A8A377352765D39B6CCFE34A63EB8A5B1C0E5F; property20=092AAE0419569843B3CD298E8DBC65729CFBE2AFD2320D2595C310BA5E0172C3A4647F90F446F467'
# response = requests.get(base_url)
# print(response)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.111 Safari/537.36 ",
    'cookie': cookie
}
i = 1
for url in base_url:
    res = requests.get(url, headers=headers).text[16:-2:1]
    # print(res)
    # print(json.loads(res)['data']['photos'])
    photos = json.loads(res)['data']['photos']
    # print(photos[0])

    for photo in photos:
        # print(photo)

        name = photo['ownerName']
        # print(photo['ownerName'])
        # print(photo['ownerUin'])
        # print(photo['url'])
        data = requests.get(photo['url']).content
        # print(data)
        name_list.append(name)
        # print(photo['ownerName'])
        with open('F:/绿协/种植统计表/第二次/' + str(i) + '-' + name + '.jpg', 'wb')as f:
            f.write(data)
        i += 1
name_list = set(name_list)
num = 1
for i in name_list:
    print(num, '\t', i)
    num += 1
