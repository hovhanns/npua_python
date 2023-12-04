import requests
import json 


url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.status_code)

data = response.json()
print(data)
for d in data:
    # print(d['title'])
    pass
# print(type(response.text))