import requests
from bs4 import BeautifulSoup as bs

url = 'http://172.16.1.3:8002/index.php?zone=lan'

def isConnected():
    res = requests.get(url)
    connected = 'Disconnect' in res.text
    return connected

def connect():
    login_payload = {'redirurl': 'https://mnit.ac.in',
           'zone': 'lan',
           'auth_user': '',# your network login id
           'auth_pass': '',# your network login password
           'accept': 'LOGIN'}
    r = requests.post(url,data=login_payload)
    
def disconnect():
    url2 = 'http://172.16.1.3:8002/'
    res = requests.get(url)
    html = bs(res.text)
    logout_id = html.find('input')['value']
    logout_payload = {
        'logout_id': logout_id,
        'zone': 'lan',
        'logout': 'Disconnect'
        }
    r = requests.post(url2,data=logout_payload)

if isConnected()==False:
    connect()