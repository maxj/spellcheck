import requests

r = requests.post('http://127.0.0.1:5000/check', data = {'word':'spelling'})

print r.status_code
print r.text

r = requests.post('http://127.0.0.1:5000/check', data = {'word':'speling'})

print r.status_code
print r.text
