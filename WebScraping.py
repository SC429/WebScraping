# libraries
import urllib.request  #installed on command line using pip
from bs4 import BeautifulSoup  # installed on command line using pip
import csv
import re

url =  ['https://www.pacificcoffee.com/find-a-store/']

data = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data.append(['Region', 'Address', 'Room', 'Time', 'Phone Number'])

for pg in url:
    page = urllib.request.urlopen(pg)
    soup = BeautifulSoup(page.read(), 'html.parser')
    table = soup.find_all('div', attrs={'class':'info-section'})

    print(table)

    for row in table:
        location = row.find('div', attrs={'class':'location'})
        location1 = location.text.strip()
        data1.append(location1)

        address = row.find('div', attrs={'class':'address'})
        address1 = address.text.strip()
        data2.append(address1)

        hours = row.find('div', attrs={'class':'business_hour'})
        hours1 = hours.text.strip()
        data3.append(hours1)

data.append([data1, data2, data3])
print(data)

with open('PacificCoffee.csv','w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)
