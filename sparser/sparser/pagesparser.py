from sutil import *
import urllib
from bs4 import BeautifulSoup
import multiprocessing as mp
import signal

# Function to call when call times out
def signal_handler(signum, frame):
    '''
        Used a signal handler for the processes to terminate the 
        process ad predefined interval.
    '''
    # Completely ingore anythin here.  This is a simple callback
    # function for signal hadler
    pass


# Function to parse a single URL and return askee text 
# Accepts single well formed URL
# Returns text representation of a url cleand from non-ascii chars and punctuation
def __parsepage__(url, timeout=30):
    '''
        Accepts a url and returns a dictionary containing word count of
        words contained in the page pointed by the url passed in as
        a parameter to this function.
    '''
    try:
        # Setting up timeout for each call
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(timeout)

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
    '''
        Processes a list of URL and retuns a list of dictionaries containing
        containing word counts from the the web pages pointed to by the urls
        contained in the list passed in as a parameter to this function.
    '''
    pool = mp.Pool(processes=procs)
    results = [pool.apply_async(__parsepage__, args=(x, )) for x in lst]
    to_return = [p.get() for p in results]
    return to_return


# Function to test code on this page
if __name__ == "__main__":
    lst = ['https://news.google.com', 'https://news.yahoo.com','http://www.msn.com', 'http://finance.google.com']
    page_text = parsepages(lst)
    print len(page_text)
    print "Length"
    for i in page_text:
        print i
    
    


