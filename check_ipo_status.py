#!/usr/bin/env python

import json
import os
import sys
import requests
import urllib3
import xml.etree.ElementTree as ET

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
PAN = None

with open(os.path.join(os.path.expanduser("~"), '.pan_card')) as file_:
    PAN = file_.read().rstrip("\n")

if not PAN:
    sys.exit("Unable to read PAN from ~/.pan_card file")

base_url = "https://linkintime.co.in/ipo/IPO.aspx"

headers = {
    'content-type': "application/json",
    'Accept': "application/json",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:81.0) Gecko/20100101 Firefox/81.0',
}

get_company_details_url = "%s/GetDetails" % base_url
response = requests.request("POST", get_company_details_url, headers=headers, verify=False)
if not response.ok:
    sys.exit("Failed to gather information from company details from %s" % get_company_details_url)

response_data = response.json()

tabular_data = ET.fromstring(response_data['d'])
if not tabular_data:
    sys.exit("Failed to parse XML data returned")

company_ids = []

for table in tabular_data:
    for element in table:
        if element.tag == 'company_id':
            company_ids.append(element.text)


def get_ipo_status(company_id=None):
    if not company_id:
        return {}

    url = "%s/SearchOnPan" % base_url

    payload = {'clientid': company_id, 'PAN': PAN, 'CHKVAL': '1'}

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)

    if not response.ok:
        print("Failed to gather information from URL %s" % url)
        return {}

    response_data = response.json()

    tabular_data = ET.fromstring(response_data['d'])
    if not tabular_data:
        print("Failed to parse XML data returned")
        return {}

    parsed_data = {}

    for element in tabular_data[0]:
        parsed_data[element.tag] = element.text

    return parsed_data


for comp_id in company_ids:
    data = get_ipo_status(company_id=comp_id)
    if data:
        print(data)
