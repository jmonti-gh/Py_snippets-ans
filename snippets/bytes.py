''' bytearrays'''

print('HOuse')

tl = (b'')
print(tl, type(tl))

Temphex = [b'\x01\x03\x04\x18X\xa8\xb0\x03']
print(Temphex, type(Temphex))
print(Temphex[0], type(Temphex[0]))
for it in Temphex[0]:
    print(it, type(it), hex(it), type(hex(it)))
print()
print(int('a8', 16))
print(Temphex[0].find(ord('X')))
print(ord('X'))
print(Temphex[0][4:])
print()
# print(dir(bytes()))
# dir(list())
trin = '134X'
print(bytes(trin, 'utf-8'))
print(bytearray(trin, 'utf-8'))

print()
tba = bytearray(Temphex)
print(tba, type(tba))


search_Temphex = Temphex.find("x",3,7)

print(search_Temphex)