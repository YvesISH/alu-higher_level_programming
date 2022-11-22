#!/usr/bin/python3
"""A script that takes GitHub credentials."""


if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    auth = HTTPBasicAuth(username=username, password=token)
    response = requests.get(url, auth=auth)
    result = response.json()
    print(result.get('id'))
