import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')

images = bsObj.find_all('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

print(bsObj.find_all(lambda tag: len(tag.attrs) == 2))
