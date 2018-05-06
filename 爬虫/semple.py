import requests

url = "https://blog.csdn.net/api/articles?type=new&category=cloud"
r = requests.get(url, timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.json())