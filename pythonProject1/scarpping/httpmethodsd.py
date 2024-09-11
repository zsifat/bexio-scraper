import requests
from requests.exceptions import RetryError
from requests.adapters import HTTPAdapter


github_adapter=HTTPAdapter(max_retries=2)

session=requests.Session()

session.mount('https://api.github.com',github_adapter)
try:
    response=session.get('https://api.github.com/')
except RetryError as err:
    print(err)
finally:
    print(response.text)
    session.close()
