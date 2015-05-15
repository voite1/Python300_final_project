from sparser.urlsparser import parseurls
from sparser.pagesparser import parsepages
from sparser.sutil import mergedicts

# Getting list of URL's from the entry url 
def geturls(url, level=1, threads=4):
	lst = parseurls(url, level, threads)
	return lst

# Getting page text from the lst of urls
def getpagetext(urllist, threads=4):
    lst = parsepages(urllist, threads)
    return lst

# Merging a list of dictionaries containing page text word counts
def mergedictlist(lst):
	dct = mergedicts(lst)
	return dct
