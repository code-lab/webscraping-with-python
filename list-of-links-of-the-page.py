from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)

def get_scrap_data():
    html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
    bs = BeautifulSoup(html.read(), "html.parser")
    main_content = bs.find("div", {
        "id": "bodyContent"
    })
    links = main_content.find_all("a")
    formatted_links = []
    for l in links:
        if l.get_text() is not "":
            formatted_links.append(l)
    return formatted_links


@app.route('/')
def main():
    links = get_scrap_data()
    mylist = "<ul>";
    for l in links:
        if 'href' not in l.attrs:
            continue
        mylist += "<li>" + "<a href=\"" + l.attrs['href'] + "\">" + l.get_text() + "</a></li>"
    mylist += "</ul>";
    return mylist
