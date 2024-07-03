



# csv for csv file handing;

import csv
with open('data.csv', mode = 'w' , newline = '' )as file:
    writer = csv.writer(file)
    writer.writerow(['name' , 'age'])
    writer.writerow(['alice', '30'])