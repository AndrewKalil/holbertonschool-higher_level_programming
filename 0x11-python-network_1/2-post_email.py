#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response"""


if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    var = urllib.parse.urlencode({'email': sys.argv[2]})
    var = var.encode('ascii')
    request = urllib.request.Request(sys.argv[1], var)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode("utf-8", "replace"))

