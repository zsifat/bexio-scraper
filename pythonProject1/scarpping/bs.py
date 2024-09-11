from email.header import Header
from pickletools import pydict
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

deptlinks=[]
html=urlopen('https://www.sust.edu/academics/schools')
bs=BeautifulSoup(html,'lxml')
dept_links=bs.find_all('a',href=re.compile(r'https://www.sust.edu/d/\w{3}$'))
for dept in dept_links:
    link=dept['href']
    deptlinks.append(link)
deptlinks.append('https://www.sust.edu/institutes/iict/faculty')
print(deptlinks)
print(len(deptlinks))
faculty_links=[]
all_faculty=[]
for links in deptlinks:
    faculty_link=links+'/faculty'
    faculty_links.append(faculty_link)
print(faculty_links)
for url in faculty_links:
    html=urlopen(url)
    bs=BeautifulSoup(html,'lxml')
    faculty_names=bs.find('div',class_='department-faculty').find_all('h4')
    for faculty in faculty_names:
        name=faculty.get_text().strip()
        all_faculty.append(name)


print(all_faculty)
print(len(all_faculty))
faculty_on_leave=[]
lecturer=[]
assistant_prof=[]
associate_prof=[]
professor=[]
head=[]
director=[]
for member in all_faculty:
    print(member)
    if '(On Leave)' in member:
        faculty_on_leave.append(member)
    if '(On Lien)' in member:
        faculty_on_leave.append(member)
    if 'Lecturer' in member:
        lecturer.append(member)
    if 'Assistant Professor' in member:
        assistant_prof.append(member)
    if 'Associate Professor' in member:
        associate_prof.append(member)
    if 'Professor' in member:
        professor.append(member)
    if 'Head' in member:
        head.append(member)
    if 'Director' in member:
        director.append(member)

prof=len(professor)-(len(assistant_prof)+len(associate_prof))
print('On leave:',len(faculty_on_leave))
print('Lecturer:',len(lecturer))
print('Assistent Professor:',len(assistant_prof))
print('Associate Professor',len(associate_prof))
print('Professor',prof)


import matplotlib.pyplot as plt
labels=['Lecturer','Assistant Professor','Associate Professor','professor']
values=[len(lecturer),len(assistant_prof),len(associate_prof),len(professor)]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0, 0, 0, 0)

plt.figure(figsize=(16,16))
plt.pie(values,explode=explode,labels=labels,colors=colors)

plt.axis('equal')
plt.title('Pie Chart')
plt.show()



# Data for the bar chart
labels = ['Lecturer', 'Assistant Professor', 'Associate Professor', 'Professor']
values = [len(lecturer), len(assistant_prof), len(associate_prof), prof]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=colors)

# Add title and labels
plt.title('Faculty Distribution by Rank')
plt.xlabel('Faculty Rank')
plt.ylabel('Number of Faculty')

# Show the plot
plt.show()


# Data for the bar chart
labels = ['On leave', 'Present']
values = [len(faculty_on_leave), (len(all_faculty)-len(faculty_on_leave))]
colors = ['red', 'green']

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=colors)

# Add title and labels
plt.title('Leave vs Present')
plt.xlabel('state')
plt.ylabel('Number of Faculty')

# Show the plot
plt.show()


