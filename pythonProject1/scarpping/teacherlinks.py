from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



deptfacultylinks=[]
html=urlopen('https://www.sust.edu/academics/schools')
bs=BeautifulSoup(html,'lxml')
dept_links=bs.find_all('a',href=re.compile(r'https://www.sust.edu/d/\w{3}$'))
for dept in dept_links:
    link=dept['href']
    link+='/faculty'
    deptfacultylinks.append(link)
deptfacultylinks.append('https://www.sust.edu/institutes/iict')
print(deptfacultylinks)

for deptfacultylink in deptfacultylinks:
    url=urlopen(deptfacultylink)
    soup=BeautifulSoup(url,'lxml')
    teacherlinks=soup.find_all('a',href=re.compile(r'https://www.sust.edu/d/arc/faculty-profile-detail/\d+$'))
    print(teacherlinks)

