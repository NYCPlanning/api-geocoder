import requests

url = 'http://0.0.0.0:5000/' 


files={'geo_file': open('geocode.py','rb'),
      'env_file': open('.env','rb')}
x = requests.post(url, files=files)
print(x.text)