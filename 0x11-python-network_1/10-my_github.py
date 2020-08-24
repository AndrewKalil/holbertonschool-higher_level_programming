#!/usr/bin/python3
"""takes your Github credentials (username and password)
and uses the Github API to display your id"""


if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(username, password))
    if req.status_code >= 400:
        print('None')
    else:
        print(req.json().get('id'))
