#!/usr/bin/python3

import requests

session = requests.Session()
response = session.get('https://google.com')
print(session.cookies.get_dict())

