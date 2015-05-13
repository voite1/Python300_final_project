import multiprocessing as mp
from sparser.urlsparser import parseurls
from sparser.pagesparser import parsepages
from sparser.pagesparser import __parsepage__
from sparser.sutil import clean
import pickle
import datetime

def test():
    lst = parseurls("https://news.google.com")


    pool = mp.Pool(processes=20)
    results = [pool.apply_async(__parsepage__, args=(x,)) for x in lst]
    output = [p.get() for p in results]
    print(len(output))
    for i in output:
    	print len(i)



if __name__ == "__main__":
    test()
