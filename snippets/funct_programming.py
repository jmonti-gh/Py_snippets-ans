# Python supports functional programming to some extend, for example:

def sayhi(name):
    return "Hi " + name

v = sayhi
print(v("Marce"))


def apply_twice(f, x):
    return f(f(x))

print(apply_twice(v, "world"))


