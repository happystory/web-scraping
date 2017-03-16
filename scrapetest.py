from urllib.request import urlopen
html = urlopen('http://192.168.0.101:8002/static/pointer.html')
print(html)
