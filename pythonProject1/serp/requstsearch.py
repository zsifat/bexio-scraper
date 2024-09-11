import re

import requests
from bs4 import BeautifulSoup
from fontTools.mtiLib import parseMarkToLigature

response=requests.get('https://www.google.com/search?q=Estate+agent+AND+Manchester+%22%40gmail.com%22+OR+%22%40yahoo.com%22+OR+%22%40hotmail.com%22+OR+%22%40aol.com%22+OR+%22%40hotmail.co.uk%22+OR+%22%40hotmail.fr%22+OR+%22%40msn.com%22+site%3Ainstagram.com&sca_esv=cd905eee47e8a54c&sca_upv=1&biw=1912&bih=968&sxsrf=ADLYWIK_aSwHBntvs-sKVLB3Nfq2d1teEw%3A1725960617140&ei=qRHgZsOjCO_O1e8P7ZqbmQ4&ved=0ahUKEwiDnOyriLiIAxVvZ_UHHW3NJuM4WhDh1QMIDw&oq=Estate+agent+AND+Manchester+%22%40gmail.com%22+OR+%22%40yahoo.com%22+OR+%22%40hotmail.com%22+OR+%22%40aol.com%22+OR+%22%40hotmail.co.uk%22+OR+%22%40hotmail.fr%22+OR+%22%40msn.com%22+site%3Ainstagram.com&gs_lp=Egxnd3Mtd2l6LXNlcnAingFFc3RhdGUgYWdlbnQgQU5EIE1hbmNoZXN0ZXIgIkBnbWFpbC5jb20iIE9SICJAeWFob28uY29tIiBPUiAiQGhvdG1haWwuY29tIiBPUiAiQGFvbC5jb20iIE9SICJAaG90bWFpbC5jby51ayIgT1IgIkBob3RtYWlsLmZyIiBPUiAiQG1zbi5jb20iIHNpdGU6aW5zdGFncmFtLmNvbUgAUABYAHAAeACQAQCYAQCgAQCqAQC4AQzIAQCYAgCgAgCYAwCSBwCgBwA&sclient=gws-wiz-serp')
bs=BeautifulSoup(response.text,'lxml')
htmlstr=bs.prettify()
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails=re.findall(email_pattern,htmlstr)
print(emails)

