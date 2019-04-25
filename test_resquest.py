import requests
proxies = {
    'https': 'http://172.16.12.201:3128',
    'http': 'http:172.16.12.201:3128'
}
# resp = requests.get('https://httpbin.org/ip')
resp = requests.get('https://httpbin.org/ip', proxies=proxies)
print(resp.text)