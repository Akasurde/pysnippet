"""
Example 4
File upload
"""

import requests
import const

files = {'file': open('sample.txt', 'rb')}
r = requests.post(const.url + "/example4/", files=files)
if r.status_code == requests.codes.ok:
    print(r.json()['msg'])