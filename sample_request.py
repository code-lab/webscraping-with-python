from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(type(html), type(html.read()), html.read())
