import requests


def check_response(url):
    response = requests.get(url)
    print(response.status_code)
