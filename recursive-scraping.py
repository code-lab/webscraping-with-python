from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
from flask import Flask

random.seed(datetime.datetime.now())
app = Flask(__name__)



def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                                                           href=re.compile("^(/wiki/)((?!:).)*$"))

@app.route('/')
def index():
    links = getLinks("/wiki/Kevin_Bacon")
    response = "<ol>"
    count = 1
    while len(links) > 0:
        if count > 10:
            break
        else:
            count += 1

        ind = random.randint(0, len(links)-1)
        new_article_link = links[ind].attrs["href"]
        new_article_text = links[ind].get_text()
        response += "<li><a href='{}'>{}</a></li>".format(
            new_article_link,
            new_article_text
        )
        links = getLinks(new_article_link)
    response += "</ol>"
    return response

if __name__ == "__main__":
    app.run()
