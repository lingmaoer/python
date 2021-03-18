import requests

for num in range(0, 11):
    url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20' \
          f'&page_start={num * 20} '

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}

    response = requests.get(url, headers=headers).json()
    #print(response.text)

    # print(response['subjects'])

    texts = response['subjects']

    for i in texts:
        # print(i)

        title = i['title']

        rate = i['rate']

        # print(title,rate)

        with open('text.csv', 'a+')as f:
            f.write(title + ',' + rate + '\n')

            print(title, rate)
