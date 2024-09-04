import requests

url = 'https://www.thecolorapi.com/id'
file_path = './download.jpg'

with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.json())
 
