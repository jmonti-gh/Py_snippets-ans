#

import psutil as pu

#print(dir(pu))

#!/usr/bin/env python

# gives a single float value
print()
print('pu.cpu_percent():', pu.cpu_percent())

# gives an object with many fields
print()
print('pu.virtual_memory():', pu.virtual_memory())

# you can convert that object to a dictionary 
dvm = dict(pu.virtual_memory()._asdict())

# you can have the percentage of used RAM
pu.virtual_memory().percent
79.2

# you can calculate percentage of available memory
pu.virtual_memory().available * 100 / pu.virtual_memory().total
20.8

print()
for k, v in dvm.items():
    print(k, ':', v)

#print(dvm)
print()
print('( tot - avail) / 100:  ', (dvm['total'] - dvm['available']) / 100)
print(' 2 ** 24', 2 ** 24)
