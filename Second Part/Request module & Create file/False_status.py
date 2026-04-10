import requests

url = requests.get("https://httpbin.org/status/404")
print("Status code:", url.status_code)
print(url.ok)
