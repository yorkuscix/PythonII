# this is a comment. Python ignores these lines

def f(x: float):
    if x<0:
        return "negative"
    if x==0:
        return "zero"
    if x>0 and x<100:
        return "small positive"
    if x>=100:
        return "large positive"

# g returns the middle element in the list l
def g(l: list):
    length_of_l = len(l)
    midpoint = int(length_of_l/2)
    return l[midpoint]

# challenge function: try to figure out how this function works
def e(s, n):
    if n==0:
        return s
    if n!=0:
        return e(s+1, n-1)