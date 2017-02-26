"""
Example 6
Session management
"""
import requests
import const

"""
Without Session
r = requests.get(const.url + "/example6/index")
if r.status_code == requests.codes.ok:
    print(r.json()['msg'])

r = requests.post(const.url + '/example6/login', data=const.formdata)
if r.status_code == requests.codes.ok:
    print(r.json()['msg'])
else:
    print r.status_code

r = requests.get(const.url + "/example6/index")
if r.status_code == requests.codes.ok:
    print(r.json()['msg'])

With Session
"""
s = requests.Session()
r = s.get(const.url + "/example6/index")
if r.status_code == requests.codes.ok:
    print(r.json()['msg'])

r = s.post(const.url + '/example6/login', data=const.formdata)
if r.status_code == requests.codes.ok:
    print(r.json()['msg'])
else:
    print r.status_code

r = s.get(const.url + "/example6/index")
if r.status_code == requests.codes.ok:
    print(r.json()['msg'])
