# Reading CSV file
from csv import DictReader

with open(r'C:\Users\mbadh\Desktop\Data Mining\DM\Sales Records.csv') as r:
    csv_file = DictReader(r)
    region = set()
    for row in csv_file:
        region.add(row['Region'])
    print(region)