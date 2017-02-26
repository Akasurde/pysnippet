"""
Example 2
Simple POST
"""
import requests
import const


r = requests.post(const.url + "/example2/json", data=const.formdata)
print(r.status_code)
print(r.json())
