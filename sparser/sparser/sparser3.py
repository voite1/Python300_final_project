import sys
import urllib
import urlparse
from bs4 import BeautifulSoup
from sutil import *

class URLRetriever(object):

    def __parseurl__(self, url):
        # list to accumulate links from the url
        my_list = []
        
        try: 
            # Getting single web page
            myopener = urllib.FancyURLopener()
            myopener.version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'
            page = myopener.open(url)
            text = page.read()
            page.close()
        
            # Parsing web page and finding URL's
            soup = BeautifulSoup(text)
            for tag in soup.findAll('a', href=True):
                tag['href'] = urlparse.urljoin(url, tag['href'])

                # adding URL's to the list
                my_list.append(tag['href'])

            # return unique list of URLs
            return set(my_list)

        except Exception as e:
            # return None on any error
            return None

    def parseurls(self, url, level=1):
        # Work with levels.  Allow up to 3 level
        if (level > 3 or level < 1):
            raise ValueError("\'level\' must have values between 1 and 3")
        # Processing for level 1
        if (level == 1):
            return set(self.__parseurl__(url))
        # Processing for level 2
        if (level == 2):
            pass
        # Processing for level 3
        if (level == 3):
            pass
        

if __name__ == "__main__":
    url = 'https://news.google.com'
    obj = URLRetriever()
    lst = obj.parseurls(url)
    if lst is not None:
        print len(lst)