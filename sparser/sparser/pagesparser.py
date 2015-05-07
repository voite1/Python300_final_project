from sutil import *
import urllib
from bs4 import BeautifulSoup
from joblib import Parallel, delayed


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


# Function to extract
def parsepages(lst, processes=4):
    to_return = Parallel(n_jobs=processes)(delayed(__parsepage__)(i) for i in lst)
    return to_return


if __name__ == "__main__":
    lst = ['https://news.google.com', 'https://news.yahoo.com','http://www.msn.com']
    page_text = parsepages(lst)
    print len(page_text)
    
    


