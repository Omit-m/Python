import requests

url = "https://picsum.photos/300"   # direct image source
response = requests.get(url)

if response.status_code == 200:
    with open("pic.jpg", "wb") as file:
        file.write(response.content)
    print("Image downloaded successfully ✅")
else:
    print("Failed to download image ❌")


