import requests

# request api key from deconz
payload = '{"devicetype": "zakapp"}'
r = requests.post("http://192.168.1.45:40850/api", data=payload)
print(r.json())
