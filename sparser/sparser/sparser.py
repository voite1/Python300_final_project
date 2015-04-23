import re
import sys
import urllib
import urlparse
from bs4 import BeautifulSoup
from sutil import *

myopener = urllib.FancyURLopener()
myopener.version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'

class URLCollector(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'

    def processurl(self, url):
        page = self.open(url)
        text = page.read()
        page.close()

        lst = []
 
        soup = BeautifulSoup(text)
        for tag in soup.findAll('a', href=True):
            tag['href'] = urlparse.urljoin(url, tag['href'])
            lst.append(tag['href'])
        return set(lst)
        

if __name__ == "__main__":
    g = URLCollector()
    my_list = g.processurl('https://news.google.com')
    print len(my_list)
    
