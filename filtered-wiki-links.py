from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from flask import Flask


app = Flask(__name__)

def get_scrapped_data(url):
    """
    Rules:
    1. They reside within the div with the id set to bodyContent
    2. The URLs do not contain semicolons
    3. The URLs begin with /wiki/
    """
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(), "html.parser")
    internal_links = []

    for link in bs_obj.find(
            "div", {
                "id":
                "bodyContent"
            }
    ).findAll(
        "a",
        href=re.compile("^(/wiki/)((?!:).)*$")
    ):
        internal_links.append(link)

    return internal_links



@app.route('/')
def main():
    url="http://en.wikipedia.org/wiki/Kevin_Bacon"
    res = "<a href='{}'>{}</a>".format(url,url)
    res += "<ol>"
    for l in get_scrapped_data(url):
        if 'href' in l.attrs:
            res += "<li>"
            res += "<a href='https://en.wikipedia.org/wiki/{}'>{}</a>".format(l.attrs['href'], l.get_text())
            res += "</li>"
    res += "</ol>"
    return res
