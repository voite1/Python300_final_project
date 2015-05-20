from sparser.urlsparser import _parseurls
from sparser.pagesparser import _parsepages
from sparser.sutil import _mergedicts
from sparser.test.selftest import _runtests

# Getting list of URL's from the entry url 
def geturls(url, level=1, threads=4):
    lst = _parseurls(url, level, threads)
    return lst

# Getting page text from the lst of urls
def getpagetext(urllist, threads=4):
    lst = _parsepages(urllist, threads)
    return lst

# Merging a list of dictionaries containing page text word counts
def mergedictlist(lst):
    dct = _mergedicts(lst)
    return dct

# Call unit tests
def sparsertest():
    _runtests()
