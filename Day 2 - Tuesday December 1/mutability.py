def are_ints_mutable(x: int):
    x = -9999

def are_lists_mutable(lst: list):
    lst[0] = -9999

def back_of_the_line(lst: list):
    first = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i+1]
    lst[-1] = first
