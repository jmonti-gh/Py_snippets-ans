### read_csv.py

'''
pandas.read_csv  -- ok!
numpy read csv -- ¿?
'''

import csv
#replace 'customers.csv' with your filename or path to file (i.e. /Desktop/folder/file.csv)
with open('customers.csv', newline='') as csvfile:
    cust_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in cust_reader:
        print(', '.join(row))

# work HERE in error Error tokenizing data. C error: Expected 11 fields in line 8, saw 12
#  - ok with Customer-DEMO_2023.csv
import pandas as pd
df = pd.read_csv('customers.csv')
print(df)