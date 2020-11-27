import math

def a(n):
    lst = []
    for i in range(n):
        lst.append(i)
    t = f(lst)
    return t

def f(new_lst):
    t = 0
    for i in new_lst:
        t = t + g(i)
    return math.sqrt(t)

def g(item):
    return item * item