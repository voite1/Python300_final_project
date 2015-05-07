import sys
import urllib
import urlparse
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
from sutil import *



def __parseurl__(url):
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

def parseurls(url, level=1, processes=4):
    # Work with levels.  Allow up to 2 levels
    if (level > 5 or level < 1):
        raise ValueError("\'level\' must have integer values between 1 and 2. Default is 1")
    # Check processes
    if (processes > 50 or processes < 1):
        raise ValueError("\'processes'\ must have integer values between 1 and 20. Defalt is 4")
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

def __contactnatelists__(list1, list2):
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


def __is_ascii__(s):
    return all(ord(c) < 128 for c in s)
        

if __name__ == "__main__":
    url = 'https://news.google.com'
    lst = parseurls(url, 2, 20)
    print len(lst)
    with open('urls.txt', 'w') as output:
        for i in lst:
            output.write(i + "\n")
    
    lines = []
    with open('urls.txt', 'rb') as inp:
        lines = inp.readlines()

    print len(lines)
    print "Done!!!"