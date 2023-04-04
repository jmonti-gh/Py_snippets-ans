# Was bron to make a snippet to get de Exception position in the tree
# and morr

# Three ways to obtain exception obj. from string w/same name
# 1. eval(): risky - discarded:
# https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object

'''
es = "IndexError"
print(es, type(es), id(es), sep=" \t ")
eo = eval(es)
print(eo, type(eo), id(eo), sep=" \t ")
print("look", "this:", "sep=", sep=" \ ")
'''

## 2 & 3: https://stackoverflow.com/questions/67909829/python-how-to-get-exception-as-an-object-from-a-string-with-the-same-name
# 2. create a function -
'''
def find_child_class(base, name):
  if base.__name__ == name:
    return base

  for c in base.__subclasses__():
    result = find_child_class(c, name)
    if result:
      return result
'''

# 3. getattr and globals() -
es = "KeyError"
print(es, type(es), id(es), sep=" \t ")
eo = getattr(globals()['__builtins__'], es)
print(eo, type(eo), id(eo), sep=" \t ")
print("look", "this:", "sep=", sep=" \ ")

# 4.
print()
import builtins as btin
#print(dir(builtins))
for ex in dir(btin):
    if ex == es:
        print(ex, type(ex))
        getattr(['__builtins__'], es)


