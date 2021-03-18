import urllib.request
import re
import random

uapools = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",
]
def ua(uapools):
    thisua=random.choices(uapools)
    headers = ("User-Agent",thisua)
    opener = urllib.request.build_opener()
    opener.addheaders=[headers]

    urllib.request.install_opener(opener)


