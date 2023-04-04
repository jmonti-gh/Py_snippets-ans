# see 'str'[::-1]
# also something i dream... ¿?

t1 = "Namespaces are one honking great idea -- let's do more of those!"
t2 = 'Los espacios de nombres son una gran idea, ¡hagamos más de esos!'
t3 = 'get'

##t3l = list(t3)
##print(t3l.reverse())
##print(t3l)
##t3r = "".join(t3l)
##print(t3r)
##
###for tx in [t1, t2, t3].reverse():


for tx in [t3, t2, t1]:
    txl = list(tx)
    txl.reverse()
    tx = "".join(txl)
    print(tx)

# cannot reverse set cause they are unorderer collection
# dic - new dic...
print()
dic = {7: True, 'j':  4.5, False: 0, 6.3: "K"}
print(dic)

dl = list(dic)
dl.reverse()
print(dl)
dr = {}
for k in dl:
    dr[k] = dic[k]

print(dr)
dic = dr
print(dic)
    
# tuple - new tuple
