#!/usr/bin/python3
"""A script that takes GitHub credentials."""


if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = 'https://api.github.com/user'
    user = sys.argv[1]
    xyz = sys.argv[2]
    authori = HTTPBasicAuth(username=user, password=xyz)
    response = requests.get(url, authori=author)
    result = response.json()
    print(result.get('id'))
