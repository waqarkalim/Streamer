import timeit
from urllib.request import urlopen

start = timeit.default_timer()

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def print_head(url):
    print('Starting {}'.format(url))
    data = urlopen(url).read()
    print('{}: {} bytes: {}'.format(url, len(data), data))

for url in urls:
    print_head(url)

stop = timeit.default_timer()

print(stop - start)
