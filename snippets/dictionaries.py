### https://realpython.com/sort-python-dictionary/#:~:text=Sorting%20Dictionaries%20in%20Python%201%20Using%20the%20sorted,...%206%20Converting%20Back%20to%20a%20Dictionary%20
## Sorting Dictionaries in Python:
print()

pdi = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(pdi)
print(sorted(pdi))              # [1, 2, 3, 4]
print(sorted(pdi.keys()))       # [1, 2, 3, 4]
print(sorted(pdi.values()))     # ['Jack', 'Jane', 'Jill', 'Jim']
print(sorted(pdi.items()))      # [(1, 'Jill'), (2, 'Jack'), (3, 'Jim'), (4, 'Jane')]

# Sort by key
pdi = dict(sorted(pdi.items()))    #{1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}
print(pdi)

# Sort by value
pdi = dict(sorted(pdi.items(), key=lambda item: item[1]))  #{2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}
print(pdi)


### How to merge (or concatenate) dicts, py 3.5+ - From Real Python - 
print()

d1 = {1: 10, 2: 20}
d2 = {'a': 'A', 'b': 'B'}
d3 = {5: 50, 6: 60}

big_di = {**d1, **d2, **d3}
print(big_di)



stop
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
    


