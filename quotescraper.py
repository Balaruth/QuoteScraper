from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = 'http://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

print soup.html.head.title.string

quotes = soup.findAll("p", attrs={"class": "quoteContent"})

for quote in quotes:
    print quote.text