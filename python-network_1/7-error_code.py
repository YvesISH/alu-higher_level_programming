#!/usr/bin/python3
"""Script that sends a requests and displays the body of response."""


if __name__ = "__main__":
    import requests
    import sys
    re = requests.get(sys.argv[1])
    if re.status_code < 400:
        print(re.text)
    else re.status_code >= 400:
        print("Error code: {}".format(request.status_code))
