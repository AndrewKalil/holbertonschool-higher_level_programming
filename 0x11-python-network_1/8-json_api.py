#!/usr/bin/python3
"""  takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    import sys

    if not sys.argv:
        q = ""
    elif len(sys.argv) > 1:
        q = sys.argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = req.json()
        if dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except ValueError:
        print('Not a valid JSON')

