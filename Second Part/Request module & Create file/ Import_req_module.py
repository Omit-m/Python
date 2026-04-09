import requests

url = "https://monkeytype.com/"

response = requests.get(url)
print(response.ok)

print(response.status_code)   # shows if request was successful (200 = OK)
print(response.text)          # shows the HTML content of the page