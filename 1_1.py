from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bs_obj = BeautifulSoup(html.read(), 'html.parser')
        title = bs_obj.title
    except AttributeError as e:
        return None
    return title

title = get_title('http://www.baidu.com/')

if title is None:
    print('Title could not found')
else:
    print(title)

