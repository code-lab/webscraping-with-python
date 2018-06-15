from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask
import sys

app = Flask(__name__)

def get_scrap_data(url):
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), "html.parser")

    links = bs.find_all("a")
    formatted_links = []
    for l in links:
        if l.get_text() is not "":
            formatted_links.append(l)
    return formatted_links


@app.route('/')
def main():
    url = "https://www.youtube.com/watch?v=SoaLsshJA8s"
    links = [l \
             for l in get_scrap_data(url) \
             if 'href' in l.attrs \
             if l.get_text() != ""
    ]
    mylist = "<p><b>Total Number of Links</b>: {}</p>".format(len(links))
    mylist += "<ol>";
    for l in links:
        mylist += "<li>" + "<a href=\"" + l.attrs['href'] + "\">" + l.get_text() + "</a></li>"
    mylist += "</ol>";
    return mylist
