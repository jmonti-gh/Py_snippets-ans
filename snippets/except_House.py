def fun(x):
    assert x >= 0
    return x ** 0.5

def mid_level(x):
    try:
        fun(x)
    except Error:
        raise

try:
    x = mid_level(-1)
except RuntimeError:
    x = -1
except:
    x = -2
print(x)



# Error- House - no_valid_excep_names¡?
def f():
    x, y = 1, 0
    try:
        print(x/y)
    except Error:
        print('except House - an other err?')
        raise

try:
    a = f()
except BaseException as e:
    print(e)
    print(e.args)
