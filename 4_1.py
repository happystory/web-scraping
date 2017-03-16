from urllib.request import urlopen
import json

response = urlopen('https://api.douban.com/v2/book/1220562').read().decode('utf-8')
responseJson = json.loads(response)

print(json.dumps(responseJson, indent=4, sort_keys=False, ensure_ascii=False))

