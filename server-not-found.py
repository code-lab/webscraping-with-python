from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


# construct the uri
def get_uri(
        protocol="http://",
        domain="www.pythonscraping1234.com/",
        path="pages/page1.html"
):
    return protocol + domain + path


try:
    html = urlopen(get_uri())
except HTTPError as e:
    print(e)
else:
    print("program continues")

if html is None:
    print('URL is not found')
else:
    print("Program is working fine.")
