from sutil import *
import urllib
from bs4 import BeautifulSoup
#from joblib import Parallel, delayed
import multiprocessing as mp


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
def parsepages(lst, procs=4):
    pool = mp.Pool(processes=procs)
    results = [pool.apply_async(__parsepage__, args=(x,)) for x in lst]
    to_return = [p.get() for p in results]
    return to_return


if __name__ == "__main__":
    lst = ['https://news.google.com', 'https://news.yahoo.com','http://www.msn.com']
    page_text = parsepages(lst)
    print len(page_text)
    
    


