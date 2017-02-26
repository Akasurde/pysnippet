"""
Example 1
Simple GET
"""
import requests
import const


r = requests.get(const.url + "/example1/")
print("Status Code: {0}".format(r.status_code))
print("Server returned: {0}".format(r.text))
print("Encoding: {0}".format(r.encoding))
print("Header: {0}".format(r.headers['content-type']))

r = requests.get(const.url + "/example1/json")
print("Jsonify: {0}".format(r.json()))
