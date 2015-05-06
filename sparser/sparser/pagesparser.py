from sutil import *
import urllib
from bs4 import BeautifulSoup


# Function to parse a single URL and return askee text 
# Accepts single well formed URL
# Returns text representation of a url cleand from non-ascii chars and punctuation
def __parsepage__(url):
    try:
	# Read url and loade url in teh BeautifulSoup
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
    
        # delete <script> and <style> tags
        for item in soup(["script", "style"]):
            item.extract()
        
        # Extract text representation of the page
        text = soup.get_text()
    
        # Clean the text from non-ascii chars and punctuation
        text = clean(text)
        return(text)
    except Exception as e:
        # Ignore any exception
        return('')


# Function to parse a list of urls
# Accepts a list of well formed URL's 
# Returns a single string concatenating clean text retreievd from the list of URL's
def parsepages(lst):
    s = ''
    for url in lst:
        temp = __parsepage__(url)
        if temp is not None:
            s = s + temp
    return s


if __name__ == "__main__":
    lst = ['https://news.google.com', 'https://news.yahoo.com','http://www.msn.com']
    page_text = parsepages(lst)
    print len(page_text)
    
    


