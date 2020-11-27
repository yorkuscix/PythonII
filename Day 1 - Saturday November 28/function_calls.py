import math

def l(word: str):
    total = 0
    for letter in word:
        total = total + 1
    return total

def a(word: str):
    total = 0
    for letter in word:
        if letter == 'a' or letter == 'A':
            total = total + 1
    return total

def v(word: str):
    total = 0
    for letter in word:
        if letter in 'aeiouAEIOU':
            total = total - 1
        if letter not in 'aeiouAEIOU':
            total = total + 1
    return total

def f(n: int):
    lst = []
    for i in range(n):
        lst.append(i)
    result = s(lst)
    return math.sqrt(result)

def s(new_lst: list):
    total = 0
    for i in new_lst:
        total = total + i
    return total

def d(num: float):
    count = 0
    while num > 1:
        num = num/2
        count = count + 1
    return count
