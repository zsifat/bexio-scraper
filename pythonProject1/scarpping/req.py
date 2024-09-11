import re

import requests
from requests.exceptions import HTTPError

response=requests.get("https://api.github.com/search/repositories",
                      params={'q':"language:python",'sort':'stars','order':'desc'})
respone_json=response.json()
pr=respone_json['items']
for repo in pr:
    print(f'Name: {repo['name']}')
    print(f'Description: {repo['description']}')
    print(f'Stars: {repo['stargazers_count']}')
    print('--------')
