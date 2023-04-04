# From Real Python - How to merge to dicts, py 3.5+

d1 = {1: 10, 2: 20}
d2 = {5: 50, 6: 60}

merged = {**d1, **d2}
print(merged)


### more about ---------
print()
updtd = d1.update(d2)
print(updtd)
print(d1)

print()
m = 10
d1, d2 = {}, {}
for i in range(1, 5):
    d1.update({i: i*m})
    d2.update({i+5: (i+5)*m})

print(d1)
print(d2)
    
merged = {**d1, **d2}
print(merged)

print()
def mk_val(k):
    m = 10
    if type(k) == str and len(k) == 1:
##        o = ord(k)
##        v = o * m
        v = chr(ord(k) + m)
    elif type(k) == int or type(k) == float:
        v = k * m
    else:
        v = k
    return v
        
dic = {}
for key in ("a", 2, "casa", 5.6, 3, "F"):
    dic[key] = mk_val(key)
print(dic)     

print()
a = b = c = 0
a += 5
print(a, b, c)

print()
t3 = t4 = (1,2,3)
t3 = t3 * 3
print(t3)
print(t4)

print()
sa = sb = sc = "trin"
sa += "gao"
print(sa, sb, sc)

print()
t1 = t2 = ()
for i in range(65, 72):
    t1 += chr(i),
print(t1)
print(t2)

print()
l1 = l2 = []
for i in range(65, 72):
    l1 += chr(i)
    #l1 += chr(i),
print(l1)
print(l2)

print()
t1 = t2 = ()
for i in range(6):
    t1 += i,
print(t1)
print(t2)

print()
l1 = l2 = []
for i in range(6):
    l1 += chr(i),
    #l1 += chr(i)
print(l1)
print(l2)
    


