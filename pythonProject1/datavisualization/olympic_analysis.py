import csv

from plotly.graph_objs import Bar, Layout
from plotly import offline

filename='data/olympics_dataset.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    for index,coloumn in enumerate(header_row):
        print(index,coloumn)
    genders=[]
    for row in reader:
        gender=row[2]
        genders.append(gender)
    male=genders.count('M')
    female=genders.count('F')
    cross_check_f=len(genders)-male
    male_percentage=male*100/len(genders)
    female_percentage=(100-male_percentage)
    print(f"{male_percentage:.2f}")
    print(f"{female_percentage:.2f}")

    x_values=['male','female']
    y_values=[male,female]
    bar_width=0.2
    data = [Bar(x=x_values, y=y_values, width=[bar_width, bar_width])]

    layout = Layout(
        title='Gender Distribution in Olympics',
        xaxis_title='Gender',
        yaxis_title='Count',
        bargap=0.9  # Adjust this value to control the separation between bars
    )

    offline.plot({'data': data, 'layout': layout}, filename='olympic.html')






