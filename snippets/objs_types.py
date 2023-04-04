''' The core is a funtion that can print: varname, varvalue & vartype
taking string varname as argument, then try it w/differents objs'''

# .encode() -turns tring to bytes & .decode(): vicebersa
def prt_from_var_as_str(st):    # void funct only print idvar, valvar, aand typevar
    id_colon = st + ':'
    var = eval(st)
    tyvar = "'" + type(var).__name__ + "'"  # tyvar2 = var.__class__.__name__
    print("Type: {:<8} -> {:<12}".format(tyvar, id_colon), var)

# .encode() -turns tring to bytes & .decode(): vicebersa
print()
trin = 'Pythön'
prt_from_var_as_str('trin')
#
trinbyte = trin.encode()
prt_from_var_as_str('trinbyte')
#
trinagain = trinbyte.decode()
prt_from_var_as_str('trinagain')
#
# list, tuples and thier elements
print()
l = [[i for i in range(3)] for j in range(3)]
prt_from_var_as_str('l')
l2 = ['char' if i % 2 == 0 else 3.14 for i in range(4)]
prt_from_var_as_str('l2')
t2 = tuple(l2)
prt_from_var_as_str('t2')
#
print()
for i in range(len(t2)):
    ti_str = 't2[' + str(i) + ']'
    prt_from_var_as_str(ti_str)

# future dict(), and others classes/objects ¿? 
# like elements from bytes, bytearrays...