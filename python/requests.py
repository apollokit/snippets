import requests
import re

url = f'https://confluence.v.co/display/{space_name}/{page_name}'
cookies = dict(JSESSIONID=session_id)
r = requests.get(url, cookies=cookies)
assert(r.status_code == 200)

# Output content converted to dictionary
print(r.json())

