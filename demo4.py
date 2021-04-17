import requests
import json
s = requests.Session()
r = requests.get('http://httpbin.org/get')
r1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r2 = s.get("http://httpbin.org/cookies")
r.status_code
r.headers
print(r2.text)
print(r.status_code)
print(r.headers)
print(r2.url)