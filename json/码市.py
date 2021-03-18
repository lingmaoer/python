import requests

def get_data(i):
    url='https://codemart.com/api/project?page=%s'.format(i)
    headers={"cookie":"mid=40320b49-33c5-42c6-855d-0ea3f706c990; _ga=GA1.2.1900374236.1587644554; _gid=GA1.2.1587607596.1587644554; JSESSIONID=1giu260gs8k9tl2mpqkprjqs2; user-vip=true; _gat_gtag_UA_151094431_1=1; _gat=1",
             "referer":"https: // codemart.com / projects",
             "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36 Edg/83.0.478.13",
             "accept":"application/json"
    }
    response=requests.get(url,headers=headers).json()
    # print(response['rewards'])
    rewards=response['rewards']
    for i in rewards:
        # print(i)
        name=i['name']
        roles=i['roles']
        price=i['price']
        typeText=i['typeText']
        with open("123.csv","a")as f:
            f.write(f"{name},{roles},{price},{typeText}\n")

for i in range(1,21):
    get_data(i)