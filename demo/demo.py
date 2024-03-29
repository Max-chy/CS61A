from operator import add, sub

'''
def a_plus_abs_b(a, b):
    """Return a+abs(b), but w ithout calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub(a, b)
    else:
        f = add(a, b)
    return f(a, b)

print(a_plus_abs_b(2,3))
'''
x = 2
def g():
    print(x)
    x = 3
    print(x)
g()
