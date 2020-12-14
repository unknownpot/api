import requests
url = "http://graph.facebook.com/4/picture?type=large"

r = requests.get(url)
print(r.content)

with open('sample.jpg', 'wb') as f:
    f.write(r.content)