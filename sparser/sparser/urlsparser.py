import sys
import urllib
import urlparse
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
from sutil import *


# Extracts visible text from the web page pointed to by the
# URL passed in as a parameter and returns a dictionay of word counts.
def __parseurl__(url):
    '''
       Reterns dictionary of the word counts from the page pointed to by
       the URL passed in as a parameter *url*.
    '''
    # list to accumulate links from the url
    my_list = []
    return_list = []
    
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
        for i in my_list:
            if i.startswith("http"):
                return_list.append(i)

        # Sorting unique urles
        return_list = set(return_list)
        return_list = list(return_list)

        return return_list

    except Exception as e:
        # return None on any error.  However, there should be no errors.
        # But if there is an error, the URL under processing is ignored.
        # This manifests iself when processing many urls
        return None


# Parses a list of URLs passed in as a paramter and returns
# a list of dictionaries containing word counts from the associated pages.
def parseurls(url, level=1, processes=4):
    '''
        Returns a list of word count dictionaries from the list of URL's passed in
        as *url*.  Optional *level=1* and *processes=4* specify how deep to recurse
        and how many processes to spawn.
    '''
    # Work with levels.  Allow up to 2 levels
    if (level > 5 or level < 1):
        raise ValueError("\'level\' must have integer values between 1 and 2. Default is 1")
    # Check processes
    if (processes > 100 or processes < 1):
        raise ValueError("\'processes'\ must have integer values between 1 and 100. Defalt is 4")
    # Processing for level 1
    if (level == 1):
        return set(__parseurl__(url))
    # Processing for level 2
    if (level == 2):
        level2_list = set(__parseurl__(url))
        level2_list2 = Parallel(n_jobs=processes)(delayed(__parseurl__)(i) for i in level2_list)
        level2_list2 = __flattenlist__(level2_list2)
        return_list = __contactnatelists__(level2_list2, level2_list)

        # Separating unique URL's
        return_list = set(return_list)
        return_list = list(return_list)
        return return_list


# Flattening the list of lists
def __flattenlist__(lst):
    '''
        Returns a single set containg a unique list of dictionaries built from
        the list of lists of dictionaries.
    '''
    my_list = []
    return_list = []
    for i in lst:
        if i is not None:
            my_list.extend(i)
    # Check if url starts with http://
    for j in my_list:
        if j.startswith("http://"):
            return_list.append(j.strip())
    # Returning concatenanted list
    return set(return_list)


# Concatenanes two lists checking for spaces and new line characters
# that may be in the urls
def __contactnatelists__(list1, list2):
    '''
        Concatenates two lists of urls and returns a set of unique URLs
    '''
    my_list = []
    # Check if there are no new line or spaces in both lists
    for i in list1:
        if __is_ascii__(i):
            if " " not in i:
                if "\n" not in i:
                    my_list.append(i.strip())
    for j in list2:
        if __is_ascii__(i):
            if " " not in j:
                if "\n" not in i:
                    my_list.append(j.strip())
    # Make list entries unique
    my_list = set(my_list)
    return my_list


# Checks if the string has any non-ascii characters
def __is_ascii__(s):
    '''
        Checks if a string has a non-ascii charaters 
    '''
    return all(ord(c) < 128 for c in s)
