from scrollingselenium import get_hotel_info
import csv


hotel_infos=[]
filename='scarpping/googlemap/sylhet_hotel.csv'

with open(filename,'r',encoding='utf-8') as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        url=row[1]
        hotelinfo=get_hotel_info(url)
        hotel_infos.append(hotelinfo)

filename='sylhet_hotel_info.csv'
with open(filename,'w',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['Title','Address','Phone No'])
    for infos in hotel_infos:
        writer.writerow(infos)

print(hotel_infos)