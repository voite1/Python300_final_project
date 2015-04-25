import sys
import urllib
import urlparse

import threading

from Queue import Queue


def worker_thread(url):
    l = []
    myopener = urllib.FancyURLopener()
    myopener.version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'
    page = myopener.open(url)
    text = page.read()
    page.close()
    l.append(text)
    return l

def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func

@synchronized
def __merge_list__(lst1, lst2):
    lst = lst1 + lst2
    return lst

def thread_runner(url_list):
    q = Queue(maxsize=0)
    for url in url_list:
        q.put(url)
    num_threads = 10

if __name__ == "__main__":
    out_list = []
    urls = ['https://news.google.com', 'http://news.yahoo.com', 'http://www.msn.com']
    for i in urls:
        g = worker_thread(i)
        out_list = __merge_list__(out_list, g)

    for j in out_list:
        print len(j)



