#

# split
trin = "John,Doe,42"
print(trin.split(','))
trin = "".join(trin.split(','))
print(trin)
print(trin[-2])
print(trin[-3])

# sort '351'
print()

print("".join(sorted('351')), type("".join(sorted('351'))))
print(sorted('351'))

l = list('351')
l.sort()
print("".join(l), type("".join(l)))

l = sorted(list('351'))
print("".join(l), type("".join(l)))


#
print()
print(10 != '1' + '0')

#
s = '12'
print(s[-1], type(s[-1]))
print(s[1::2], type(s[1::2]))
print(s, type(s))
