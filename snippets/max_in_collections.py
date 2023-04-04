# https://www.w3schools.com/python/python_lists.asp

'''
# Python Collections (Arrays)
There are four collection data types in the Python programming language:
- List: is a collection which is ordered and changeable. Allows duplicate
members.
- Tuple: is a collection which is ordered and unchangeable. Allows duplicate
members.
- Set: is a collection which is unordered, unchangeable*, and unindexed.
No duplicate members. (Set items are unchangeable, but you can remove
and/or add items whenever you like).
- Dictionary is a collection which is ordered and changeable. No duplicate
members.
'''

lst = [i for i in range(15) if i % 2 == 1]
print(lst," - max lst:", max(lst))

print()
tup = tuple(lst)
print(tup," - max tup:", max(tup))

print()
set_ = set(lst)
print(set_," - max set_:", max(set_))

t1 = (1120, "a")
#print(max(t1))
## TypeError: '>' not supported between instances of 'str' and 'int'
