import datetime as dtm

# Diff ways to print clear mess i found

##weight = 0.2
##animal = "newt"
##print(weight, 'kg is the weight of the ' + animal + '.')
##print('{} kg is the weight of the {}.'.format(weight, animal))
##print(f'{weight} kg is the weight of the {animal}.')
##print("%.1f kg is the weight of the %s" % (weight, animal))
##
##print()
##import math as m
##
##dic = {'weight': 0.2, 'animal': "newt", 't':'{} kg is the weight of the {}.',
##       0: False, 'pi': m.pi, True: '!= 0', 'math': dir(m)}
##
##for k,v in dic.items():
####    print('%s:\t\t%s' % (str(k), str(v)))
##    print('{}:\t\t{}\t-> {}'.format(k, v, type(v).__name__))

# try :> left algn, :< right algn and :^ center algn

n = ['Mar', 'Ignacio', 'pcacc']
m = [56, 43, 46]
p = [5.4, 17.50, 100.0]

for i in range(len(n)):
    print(f' {n[i]} {m[i]}  {p[i]}')
print()

for i in range(len(n)):
    print(f' {n[i]:>12} {m[i]:>12} {p[i]:>8} ')
print()

# https://stackoverflow.com/questions/32808383/formatting-numbers-so-they-align-on-the-decimal-point
# PEP498
# https://stackoverflow.com/questions/1025379/decimal-alignment-formatting-in-python

# data
starters = [
    [ 'Andre Iguodala', 4, 3, 7 ],
    [ 'Klay Thompson', 5, 0, 21 ],
    [ 'Stephen Curry', 5, 8, 36 ],
    [ 'Draymon Green', 9, 4, 11 ],
    [ 'Andrew Bogut', 3, 0, 2 ],
]

# define format row
row = "| {player:<16s} | {reb:2d} | {ast:2d} | {pts:6.2f}|".format

for p in starters:
    print(row(player=p[0], reb=p[1], ast=p[2], pts=p[3]))


fn = 'house.txt'
sort = 'Alphabetical'
             
dts = dtm.datetime.today().strftime('%d/%m/%Y %H:%M:%S')  # dts > string
print(f'{dts:>78}')
print()

print()
print('-. Letter frecuency analysis. - file: {}'.format(fn))
print('\t Results - {} order - {:>35}'.format(sort, dts))
print('-' * 78)
