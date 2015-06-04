import time
import pickle
import sparser
import gzip
import emailer
import datetime


def run(url='https://news.google.com'):

    # Output file name
    filename = datetime.date.today().strftime("%Y-%m-%d")
    filename = filename + ".dict.pickle.gz"

    # Get unique list of urls to process
    urllist = sparser.geturls(url, 1)
    print "Obtained", len(urllist), "unique URLs"

    my_dict = sparser.getpagetext(urllist, 20)
    print "Counted words in", len(my_dict), "web pages"

    try:
        out_handle = gzip.open(filename, "wb")
	pickle.dump(my_dict, out_handle)
	out_handle.close()
	print "Pickled output in", filename
    except Exception as e:
	print e


if __name__ == "__main__":
    run()

