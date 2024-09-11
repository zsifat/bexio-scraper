import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename='data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    for index,column_header in enumerate(header_row):
        print(index,column_header)

    dates,highs,lows=[],[],[]

    for row in reader:
        current_date=datetime.strptime(row[2], '%Y-%m-%d')

        try:
            high=int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing Data for {current_date}")

        lows.append(low)
        highs.append(high)
        dates.append(current_date)


    plt.style.use('classic')
    fig,ax=plt.subplots()

    ax.plot(dates,highs,c='red',linewidth=1,alpha=0.5)
    ax.plot(dates,lows,c='blue',alpha=0.5)
    ax.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

    plt.title("Daily high temperatures, 2018",fontsize=14)
    plt.xlabel('',fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=14)


    plt.show()