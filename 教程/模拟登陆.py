import time
import requests

url = 'https://creditcard.ecitic.com/citiccard/ucweb/toRegister.do?sid=ECCQGS010'

def get_time():
    now_time = str(int(time.time() * 1000))
    return now_time

get_time()






