import requests

r = requests.get("http://example.com")
print r.headers
print r.elapsed