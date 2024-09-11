import csv
filename_1='data/all_upwork_jobs_2024-02-07-2024-03-24.csv'
filename_2='data/all_upwork_jobs_2024-03-24-2024-05-21.csv'
filename_3='data/all_upwork_jobs_2024-05-21-2024-07-25.csv'

titles = []
with open(filename_1,encoding='utf-8') as file:
    reader1=csv.reader(file)
    for row in reader1:
        title=row[0]
        titles.append(title)
with open(filename_2, encoding='utf-8') as file:
    reader2 = csv.reader(file)
    for row in reader2:
        title=row[0]
        titles.append(title)
with open(filename_3, encoding='utf-8') as file:
    reader3 = csv.reader(file)
    for row in reader3:
        title=row[0]
        titles.append(title)

print(len(titles))

a='android app'
i=0
for title in titles:
    if a in title.lower():
        i+=1
        print(title)

print(i)



