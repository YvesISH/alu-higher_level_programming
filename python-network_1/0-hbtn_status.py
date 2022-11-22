#!/usr/bin/python3
"""python script that fetches url link."""


import urllib.request


if __name__ = '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        yy = response.read()
        print("\t- type: {}".format(type(yy)))
        print("\t- content: {}".format(yy))
        print("\t- utf8 content: {}".format(yy.decode('utf-8')))
