

import requests
import json
import os

# response = requests.get('http://localhost:5000/api/id')
# id = json.loads(response.text)['id']
zip_file = "C:\\Users\\ib4re\\Desktop\\Desktop Folders\\Upwork\\Cedric\\milestone2\\data_api\\new.zip"

headers = {
    'Content-Type': 'multipart/form-data',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br'
}

parameters = {
    "id": "TMw", 
    "upload_file" : zip_file,
}

response = requests.post('http://localhost:5000/api/upload', headers=headers, params=parameters)
print(response)
print(response.text)

