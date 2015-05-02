from sparser.urlsparser import __parseurl__
from sparser.pagesparser import __parsepage__

if __name__ == "__main__":
	text = __parseurl__("https://news.google.com")
	print len(text)
	test = __parsepage__(text)
	print len(text)