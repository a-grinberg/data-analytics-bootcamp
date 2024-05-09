
# Instructions :
# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

from pip._vendor.requests import get
from datetime import datetime

def get_response_time(url):
      start = datetime.now()  
      x = get(url)
      stop = datetime.now()
      print(stop - start)
      return f'Status{x}, time to response {stop-start}'

get_response_time('https://www.google.com/')
get_response_time('https://www.ynet.co.il/home/0,7340,L-8,00.html')
get_response_time('https://www.imdb.com/')
get_response_time('https://www.amazon.com/')
get_response_time('https://developers.institute/')