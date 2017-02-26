"""
Example 3
Response code
"""
import requests
import const


r = requests.post(const.url + "/e1xample2/json", data=const.formdata)
if r.status_code == requests.codes.ok:
    print("Successfully. Do further processing")
    if r.json()['status'] == "OK":
        print(r.json()['msg'])
else:
    print("Failed to get server request")

# https://github.com/kennethreitz/requests/blob/master/requests/status_codes.py
r = requests.get(const.url + "/nowhere")
if r.status_code == requests.codes.not_found:
    print "You found 404"
