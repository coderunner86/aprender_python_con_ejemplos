import requests
import socket 

def check_localhost():
    localhost = socket.gethostbyname('localhost')

def check_connectivity():
    request = requests.get("http://www.google.com")
    status_code = 200
    return status_code

