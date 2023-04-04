# 

x = 75

def f_ok():
    print(x)

def f_y():
    y = x + 1
    print('x:', x, '  - y:', y)

def f_bad():
    x = x + 1  # UnboundLocalError: cannot access local var
                # 'x' where it is not assoc. w/a value
    print(x)

f_ok()
f_y()
f_bad()
