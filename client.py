import requests

resp = requests.get('http://192.168.1.227:8080/hello')
print(resp.status_code, resp.text)