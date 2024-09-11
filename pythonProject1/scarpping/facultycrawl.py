from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

faculty_links={}

for x in range(1000):
    url=f'https://www.sust.edu/d/pme/faculty-profile-detail/{x}'
    html=urlopen(url)
    bs=BeautifulSoup(html,'html.parser')
    div=bs.find('div',class_='department-overview faculty-detail')
    name=div.h3.string
    if name:
        faculty_links[name]=url
        print(f'{url} : {name}')
    else:
        print('haha')
print(len(faculty_links))

filename='teacher_websites.csv'
with open(filename,mode='w',newline='',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['Teacher Name','Website'])

    for name,link in faculty_links.items():
        writer.writerow([name,link])
print(f'Data written to {filename}')