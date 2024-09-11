import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

input_filename = 'teacher_websites.csv'
output_filename = 'teacher_data.csv'

# Open the input CSV file for reading
with open(input_filename, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader, None)

    # Open the output CSV file for writing
    with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        # Write the header for the output CSV
        writer.writerow(['Teacher Name', 'Designation', 'Phone Number', 'Number of Journals'])

        for row in reader:
            link = row[1]

            html = urlopen(link)
            bs = BeautifulSoup(html, 'html.parser')

            div = bs.find('div', class_='department-overview faculty-detail')
            if div:
                teacher_name = div.h3.string if div.h3 else 'N/A'

                designation = div.find_next('p', class_='designation')
                designation = designation.string if designation else 'N/A'

                contact_info = div.find('ul', class_='contact-info-ul')
                phone_no = contact_info.find('li', string=lambda x: x and 'Phone' in x) if contact_info else None

                if phone_no:
                    phone_no = str(phone_no.string)
                    phone_numbers = re.findall(r'(\d{3}[-.\s]?\d{4}[-.\s]?\d{6}|\b\d{11}\b|^\d{3}[-.\s]?\d{10})',
                                               phone_no)
                    phone_number = phone_numbers[0] if phone_numbers else '-'
                else:
                    phone_number = '-'

                journals_conference = div.find('h4', string='Journal Publications')
                if journals_conference:
                    journals_conference = journals_conference.find_next_sibling('ol').find_all('li')
                else:
                    journals_conference = []

                # Write data to the output CSV file
                writer.writerow([teacher_name, designation, phone_number.strip(), len(journals_conference)])
                print(teacher_name)
            else:
                # Handle the case where div is not found
                writer.writerow(['N/A', 'N/A', '-', 0])


print(f"Data has been written to {output_filename}")
