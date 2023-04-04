# From IG

l = list("1234")
print(l)
l[0] = l[1] = 5
print(l)
##la = list(5)
##print(la)

l = list("1234")
trin = "".join(l)
print(l,trin)

ln = [i for i in range(1,5)]
print(ln)
##seq = "".join(ln)
ls = list(map(lambda x: str(x), ln))
print(ls)
seq = "".join(ls)
print(seq)

# deifered error?
print()
e = 'butter'
##def f(a): print(a)+e
##TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
##f('bitter')

print()
f = map(lambda z: print(bool(z%2)), (20,21))
for b in f: pass

