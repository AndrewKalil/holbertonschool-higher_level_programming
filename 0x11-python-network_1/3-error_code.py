#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the
    body of the response"""


if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))