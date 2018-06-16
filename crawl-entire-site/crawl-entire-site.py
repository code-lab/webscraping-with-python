from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime
import random
import re

from flask import Flask, request, render_template

#random.seed(datetime.datetime.now())

app = Flask(__name__)


def get_links(url):
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), "html.parser")
    links = bs.find('div', {
        'id': 'bodyContent'
    }).find_all(
        "a",
        {
            'href': re.compile('^(/wiki/)((?!:).)*$')
        }
    )
    result = []
    for l in links:
        result.append(l)
    return links


def prepare_response(links):
    response = "<ol>"
    for l in links:
        response += "<li><a href='{}'>{}</a></li>".format(l.attrs['href'], l.get_text())
    response += "</ol>"
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    url = ""
    response = ""
    if request.method == 'POST':
        url = "https://en.wikipedia.org/wiki/" + request.form['url'].strip().replace(" ", "_")

    if url is not "":
        links = get_links(url)
        response = prepare_response(links)

    return render_template('wiki-search.html', url=url, response=response)

if __name__ == "__main__":
    app.run()
