#!/usr/bin/python3
"""A script that sends POST request."""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys
    data = urlencode({"email": \
            sys.argv[2] }).encode("ascii")

    request = Request(sys.srgv[1], data)
    with urlopen(request) as re:
        print(re.read().decode('utf-8'))
