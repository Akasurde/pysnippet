"""
Example 5
Headers
"""
import requests
import const


r = requests.get(const.url + "/example1/")
print("Headers: {0}".format(r.headers))