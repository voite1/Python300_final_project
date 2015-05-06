from sparser.urlsparser import __parseurl__
from sparser.pagesparser import __parsepage__
from sparser.sutil import clean

if __name__ == "__main__":
	lst = __parseurl__("https://news.yahoo.com")
	print len(lst)

	for i, url in enumerate(lst):
		result = __parsepage__(url)
		print i, len(result)
		print "-->", len(clean(result))