import sys

import requests


def check_response(url):
    response = requests.get(url)
    print(response.status_code)


def main():
    check_response(sys.argv[1])


if __name__ == '__main__':
    main()
