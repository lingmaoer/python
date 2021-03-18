from bs4 import BeautifulSoup

soup = BeautifulSoup(html ,'lxml')

a1 = soup.find_all('a')

a2 = soup.find_all('a',limit=3)[2]

a3 = soup.find_all('a',class_ = 'aaa',id = 'fff')

a4 = soup.find_all('a',attrs={'class':'aaaa'})

a5 = soup.find_all('a').strings

a8 = soup.find_all('a').string

a6 = soup.find_all('a')['href']

a7 = soup.find('a')
for a in a7:
    a7.striped_strings










