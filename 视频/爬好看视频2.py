import requests
import json
for i in range(0,3):
    print('========%s=========='%i)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
                'cookie':'BIDUPSID=A5C34952AB564182BEC1FB557BEEEC72; PSTM=1584545116; BAIDUID=A5C34952AB56418261F9C68EC257125E:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=30963_1451_31044_21111_30823_22158; PSINO=1; COMMON_LID=8117abda7f7c1b57ec0bc254603f86af; MONGOLIA_TIME=1584621486.9772; HK_CH_EXPIRED_TIME=1584633599000; HK_CH_IS_CLICKED=0; MONGOLIA_SID=1; HK_SID=3157_1-5428_1; Hm_lvt_77ca61e523cd51ec7ac7a23bc4d24edf=1584621486; PC_TAB_LOG=haokan_website_page; HK_CH_MAT_INDEX=0; Hm_lpvt_77ca61e523cd51ec7ac7a23bc4d24edf=1584626761; HK_CH_REFRESH_TIMES=3; BDSFRCVID=i_DsJeCCxG3HHcRutk71qe2nnKfB4Z1-g_EP3J; H_BDCLCKID_SF=tR333R7oKRu_HRjYbb__-P4DHUjHfRO2X5REVhP23POkeqOJ2Mt5yMkS0loJLlQJQbR7hlOg5q_MoCDzbpnp05tpeGLsaPoy2K6XsJoq2RbhKROvhjntK6uQ-nnjhjnzX2ceaJ5n0-nnhpnS-p5h5hLsQRjPbx7TWCcG_UFhHR3rsftRy6CaePk_hURK2D6aKC5bL6rJabCQe4_ZK-brKbTMXlrCbMT-027OKKOdWnOCftbxhIFVjn-LhPOh3j3zt4jMMh5xthF0hDvd-tnO-t6H-xQ0KnLXKKOLSbQ-q4Jj_PJueUT0DbtpbtbmhU-eWgb2bt52-n7khC3gLUcTbxj3WGLLKhR4Ln7ZVDDQ2njojnjkq45HMt00qxby26Rh-Jjj3M7MMDvvjRvRy4oTLnk1DP775hjtbI0fbKng5C5ZOnQtjhCaqt-mQJ0eBjIDfKbKWbvqajrDHJTg5DTjhPr2blK_bPJd-TLsBx7g-hcqEpO9QTb1y-tw5qOWt5oD5RrXWqvD0DbAhj6TBUomDUTh-p52f6_DtJKH3J; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1584626752,1584626769,1584628057,1584628094; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1584628096; reptileData=%7B%22data%22%3A%22bf0c261a7683bc87659f08673ee3f8229134470ae515152a8fdac8ad40ea93473e161bd2fe1001aa54c03a59707894fe6c249acec88bce3e32a0a79de3294ed2a2feca39d541c747433bdc2c67cfd8efffe343fe1ba8b15a78d456484bcb9ed2dfb559f35b399406124d8ac4353dcf5f9886195a2049489a946811ed9af68e5f%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22079bd4c3%22%7D'}
    #base_url = 'https://haokan.baidu.com/videoui/api/videorec?tab=gaoxiao&act=pcFeed&pd=pc&num=20&shuaxin_id=1584623847490'
    base_url='https://haokan.baidu.com/videoui/api/videorec?tab=dongman&act=pcFeed&pd=pc&num=20&shuaxin_id=1584628096322'
    response = requests.get(base_url,headers=headers)
    data = response.text

    json_data = json.loads(data)
    data_list = json_data['data']['response']['videos']
    for data1 in data_list:
        video_title = data1["title"]+'.mp4'
        video_url = data1["play_url"]
        void_data = requests.get(video_url,headers=headers).content
        with open('vide\\'+video_title,'wb') as f:

            f.write(void_data)
            print(data1['title']+'-------下载完成-----')
