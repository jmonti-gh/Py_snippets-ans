# is vas == ; id() will help

# first w/ints you shoud thin thas 'is' is False but NO
a = 5
b = 5 # b == a  but b not is a
print("b == a:", b == a, " - b is a:", b is a)    # True - True
print("id(a):", id(a), " - id(b):", id(b))

# of course now 'is' also True
print()
primvar = s = 3
print("primvar is s:", primvar is s)     # True

# but now... change one value of one var
s //= 2
print("primvar is s:", primvar is s)     # False

# and a couple of neutral change w/ a and b ... 
print()
a += 0
print("b == a:", b == a, " - b is a:", b is a)    # True - True
print("id(a):", id(a), " - id(b):", id(b))
b *= 1
print("b == a:", b == a, " - b is a:", b is a)    # True - True
print("id(a):", id(a), " - id(b):", id(b))

# now.. change value (as integer)
a += 1
print("b == a:", b == a, " - b is a:", b is a)    # True - True
print("id(a):", id(a), " - id(b):", id(b))


# In collection data (list, touple, set, dict) and strings totally different
