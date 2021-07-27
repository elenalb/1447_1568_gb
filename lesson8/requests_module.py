import requests

resp = requests.get('https://github.com/requests')
print(resp)
print(type(resp))
print(resp.headers)
print(resp.status_code)

# data = {'key1': 'value1'}
# resp = requests.get('https://github.com/requests', param=data)
# https://github.com/requests/get?key1=value1
