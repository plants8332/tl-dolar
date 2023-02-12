import requests

req = requests.get("https://api.exchangerate.host/latest", params={"base": "USD"})

print(req.json()["rates"]["TRY"])