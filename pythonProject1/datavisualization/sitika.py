import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename='data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    header_row1=next(reader)
print(header_row)