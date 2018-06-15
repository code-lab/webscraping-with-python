from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/page1.html")
beautiful_soup = BeautifulSoup(html.read(), "html.parser")
print(beautiful_soup.body)