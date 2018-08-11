import urllib, time, requests, multiprocessing
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Process
from itertools import product
start_time = time.time()
urls = [
  'http://www.python.org',
  'http://www.python.org',
  'http://www.python.org',
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]

def openURL(url):
    return requests.get(url)


if __name__ == '__main__':
    with multiprocessing.Pool(processes=16) as pool:
        results = pool.starmap(openURL, product(urls))

    print(time.time() - start_time)
# make the Pool of workers
#pool = ThreadPool(12)

# open the urls in their own threads
# and return the results
#results = pool.map(openURL, urls)

# close the pool and wait for the work to finish
#pool.close()
#pool.join()

