def f(lst: list, i: int):
    e = lst[i]
    lst.remove(e)

def h(lst: list):
    return lst[:-3] + ['PYTHON!'] + lst[-3:]

def g1(lst: list, i: int):
    new_lst = lst[:i] + ['Hello!'] + lst[i+1:]
    return new_lst

def g2(lst: list, i: int):
    lst[:] = lst[:i] + ['Hello!'] + lst[i+1:]
    