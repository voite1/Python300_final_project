import sys
import urllib
import urlparse
from bs4 import BeautifulSoup
from sutil import *

lst = []
url = 'https://news.google.com'
myopener = urllib.FancyURLopener()
myopener.version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'
page = myopener.open(url)
text = page.read()
page.close()

soup = BeautifulSoup(text)
for tag in soup.findAll('a', href=True):
    tag['href'] = urlparse.urljoin(url, tag['href'])
    lst.append(tag['href'])

print len(set(lst))
