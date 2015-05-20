from sutil import _clean
import urllib2
from bs4 import BeautifulSoup
import multiprocessing as mp


# Function to parse a single URL and return askee text 
# Accepts single well formed URL
# Returns text representation of a url cleand from non-ascii chars and punctuation
def _parsepage(url, timeout=20):
    '''
        Accepts a url and returns a dictionary containing word count of
        words contained in the page pointed by the url passed in as
        a parameter to this function.
    '''

    try:
        # Read url and loade url in teh BeautifulSoup
        html = urllib2.urlopen(url, timeout=timeout).read()
        soup = BeautifulSoup(html)
    
        # delete <script> and <style> tags
        for item in soup(["script", "style"]):
            item.extract()
        
        # Extract text representation of the page
        text = soup.get_text()
    
        # Clean the text from non-ascii chars and punctuation
        text = _clean(text)

        # Returned cleaned text
        return text 

    except Exception as e:
        # Ignore any exception
        return('')


# Function to extract
def _parsepages(lst, procs=4):
    '''
        Processes a list of URL and retuns a list of dictionaries containing
        containing word counts from the the web pages pointed to by the urls
        contained in the list passed in as a parameter to this function.
    '''

    # Create process pool
    pool = mp.Pool(processes=procs)

    # Run threads and get the list of the results
    results = [pool.apply_async(_parsepage, args=(x, )) for x in lst]

    # Create a list of dictionaries to return
    to_return = [p.get() for p in results]

    # Return the list of dictionaries
    return to_return

    
    


