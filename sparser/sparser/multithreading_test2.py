import Queue
import threading
import urllib2

import sparser3

# called by each thread
def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

# theurls = ["http://google.com", "http://yahoo.com"]

ur = sparser3.URLRetriever()

theurls = ur.__parseurl__("https://news.google.com")
print len(theurls)

q = Queue.Queue()

try:
    for u in theurls:
        t = threading.Thread(target=get_url, args = (q,u))
        t.daemon = True
        t.start()
except Exception as e:
	pass

s = q.qsize()
print(s)