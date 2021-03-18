import requests
import re

data = requests.get("http://edu.csdn.net/huiyiCourse/detail/253").text
#print(data)
pat = "<p>(\d*?)</p>"
rest = re.compile(pat).findall(data)
print(rest[0])






