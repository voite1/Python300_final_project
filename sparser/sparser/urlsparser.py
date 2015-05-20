import sys
import urllib
import urlparse
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
from sutil import *


# Extracts visible text from the web page pointed to by the
# URL passed in as a parameter and returns a dictionay of word counts.
def _parseurl(url):
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
def _parseurls(url, level=1, processes=4):
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
        return (_parseurl(url))

    # Processing for level 2
    if (level == 2):

        # Get data out of the initial page
        level2_list = set(_parseurl(url))

        # Get urls out of the pages pointed to by the links retrevied from the first level
        level2_list2 = Parallel(n_jobs=processes)(delayed(_parseurl)(i) for i in level2_list)

        # Create a single list out of the list of lists
        level2_list2 = _flattenlist(level2_list2)

        # Concatenate links from level 1 and level 2
        return_list = _contactnatelists(level2_list2, level2_list)

        # Separating unique URL's
        return_list = set(return_list)
        return_list = list(return_list)

        # Return unique list of urls
        return return_list


# Flattening the list of lists
def _flattenlist(lst):
    '''
        Returns a single set containg a unique list of dictionaries built from
        the list of lists of dictionaries.
    '''

    # Create placeholders
    my_list = []
    return_list = []

    # Create a list ouf list of lists
    for i in lst:
        if i is not None:
            my_list.extend(i)

    # Check if url starts with http
    for j in my_list:
        if j.startswith("http"):
            return_list.append(j.strip())

    # Returning concatenanted list
    return_list = set(return_list)
    return_list = list(return_list)

    # return the list
    return return_list


# Concatenanes two lists checking for spaces and new line characters
# that may be in the urls
def _contactnatelists(list1, list2):
    '''
        Concatenates two lists of urls and returns a set of unique URLs
    '''

    # Created a list to return
    my_list = []

    # Check if there are no spaces in both lists
    for i in list1:
        if _is_ascii(i):
            if " " not in i:
                if "\n" not in i:
                    my_list.append(i.strip())

    # Check if there are no new lines in the urls
    for j in list2:
        if _is_ascii(i):
            if " " not in j:
                if "\n" not in i:
                    my_list.append(j.strip())

    # Make list entries unique
    my_list = set(my_list)
    my_list = list(my_list)

    # Return the list
    return my_list


# Checks if the string has any non-ascii characters
def _is_ascii(s):
    '''
        Checks if a string has a non-ascii charaters 
    '''
    return all(ord(c) < 128 for c in s)
