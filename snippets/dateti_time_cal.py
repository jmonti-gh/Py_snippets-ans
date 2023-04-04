#

import datetime as dtm
import time as ti
import calendar as cal

# only datetime
fn = 'house.txt'
sort = 'Alphabetical'

td = dtm.datetime.today()
print(td, type(td))
print(td.strftime('%d/%m/%Y %H:%M:%S'))

print()
#td = dtm.datetime.today()                # today > datetime obj                
dts = dtm.datetime.today().strftime('%d/%m/%Y %H:%M:%S')  # dts > string
print(f'{dts:>78}')
print()

print()
print('-. Letter frecuency analysis. - file: {}'.format(fn))
print('\t Results - {} order - {:>35}'.format(sort, dts))
print('-' * 78)
#print('-. Letter frecuency analysis. - file: {} {} {:>25}'.format(fn, 'me', dt))
print()
#print('-. Letter frecuency analysis. - file:', fn, f'{dt:>25}')



td = td.isoformat()
print(td, type(td))

tda = dtm.date.today()
print(tda, type(tda))
tda = tda.isoformat()
print(tda, type(tda))
