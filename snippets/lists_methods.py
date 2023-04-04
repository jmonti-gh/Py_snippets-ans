# lists methods alphabetic order:
'''
append()  Adds an element at the end of the list
clear()   Removes all the elements from the list
copy()    Returns a copy of the list
count()   Returns the number of elements with the specified value
extend()  Add the elements of any iterable to the end of the current list
index()   Returns the index of the first element with the specified value
insert()  Adds an element at the specified position
pop()	  Removes the element at the specified position
remove()  Removes the first item with the specified value
reverse() Reverses the order of the list
sort()    Sorts the list
'''

tri = '▲'       # 9650
sqr = '■'       # 9633
cir = '⬤'       # 11044

##print()
la = ['⬤', '■', '■']
##print("la:",la)

# .append(elm)
print()
print("-. la.append('▲'):\n")
print(la, '  -->  ', end="")
r = la.append('▲')
print(la)
print('\n & return:', r)
##print(la, "& la.append('▲') ->  ", end="")
##apr = la.append('▲')
##print(la, ' - return:', apr)
#print("la.append('▲'), then la:", la, ' - and .append() return:', apr)

# .insert(pos, elm)
print('\n' * 2, end="")
print("-. la.insert(2, '⬤'):\n")
print(la, '  -->  ', end="")
r = la.insert(2, '⬤')
print(la)
print('\n & return:', r)

# .count(elm)
print('\n' * 2, end="")
print("-. la.count('■'):\n")
print(la, '  -->  ', end="")
r = la.count('■')
print("la.count('■'):", la.count('■'))
print('\n & return:', r)

print()
i = input("Press any key to continue... ")

# .remove(elm)
print('\n' * 2, end="")
print("-. la.remove('⬤'):\n")
print(la, '  -->  ', end="")
r = la.remove('⬤')
print(la)
print('\n & return:', r)

# .pop(pos_int)
print('\n' * 2, end="")
print("-. la.pop(2):\n")
print(la, '  -->  ', end="")
r = la.pop(2)
print(la)
print('\n & return:', r)

# .extend(iterable)
print('\n' * 2, end="")
print("-. la.extend():\n")
s = {'a','c'}
t = (1.6, 2.6)
trin = ".py"
dic = {i: i * 10 for i in range(5, 7)}
print(la.extend(s), la)
print(la.extend(t), la)
print(la.extend(trin), la)
print(la.extend(dic), la)
print(la.extend(range(3)), la)
print(la)

print()
i = input("Press 'Return' to continue... ")

# rare case of 'add' (IG Quiz)
print('\n' * 2, end="")
print("-. lst += [30, 40]:\n")
la = [10, 20]
lb = la
lb += [30, 40]
lc = list(t)
print('lb = (is) la:', la, lb)
print("'+=' is same as .extend(), BUT lst = lst + seq only valid for lst + lst")
la += s     
print('lb = (is) la:', la, lb)
lb = lb + lc
print('lb = (is) la:', la, lb)
lc += range(3)
print(lc)



##print(la, '  -->  ', end="")


# don´t try clear()
# don´t try copy()

##print()
##ctr = la.count('■')
##print("la.count('■'):", la.count('■'), '(for la:', la,')',
##      ' - and .count() return:', ctr)
# 




##print(
##
##
##
##
##
##lbase = [chr(9607), chr(9632), chr(9633), chr(9650)]
##print(lbase)
##
##for i in [9607, 9632, 9633, 9650, 9652, 9670, 9679, 9698, 9699, 9673,
##          9668, 9664, 8718, 8226, 9899, 11205, 12831]:
##    print(i, chr(i), end="  ")
##print()
##
####for i in range(9728, 9841):
####    print(i, chr(i), end="\t")
####print()
##
####for i in range(65281, 65393):
####    print(i, chr(i), end="\t")
####print()
##
##tri = '▲'       # 9650
##sqr = '■'       # 9633
##cir = '⬤'       # 11044
##print(65517, chr(65517))
##
##for i in range(65532, 65534):
##    print(i, chr(i), end="\t")
##print()
##
##for i in (0xE2, 0xAC, 0xA4):
##    print(i, chr(i), end="\t")
##print()
##
####print(U+2B24)
####print(U+23FA)
####print(U+26AB)
##print(chr(9210), chr(9899), chr(11044), chr(12830))
