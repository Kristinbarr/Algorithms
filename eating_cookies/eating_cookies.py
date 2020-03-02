#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

def eating_cookies(n, cache=None):
  # add all the n-1 combinations (1 in front)
  # add all the n-2 combinations (2 in front)
  # add all the n-3 combinations (3 in front)
  # This will overwrite the array cache and replace with a dict cache
  # base case: if n is 0 or 1 return 1... if n is 2 return 2

  # 0 -> 0 cookie 1 time
  # 1 -> 1 cookie
  
  # 2 -> 1 cookie, 1 cookie
  # 2 -> 2 cookie

  # 3 -> 1 cookie, 1 cookie, 1 cookie
  # 3 -> 1 cookie, 2 cookie
  # 3 -> 2 cookie, 1 cookie
  # 3 -> 3 cookie

  if n < 0:
    return 0
  elif n == 0:
    return 1
  # if cache exists and specific n has a value, return that value
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    # if no cache, create an empty dict
    if not cache:
      cache = {}
    # else get the value, put it in the cache amd return the value
    value = eating_cookies(n-1,cache) + eating_cookies(n-2,cache) + eating_cookies(n-3,cache)
    cache[n] = value
    return value



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
