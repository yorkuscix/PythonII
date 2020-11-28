# this is a comment. Python ignores these lines

# import math allows us to use the square root function if f
import math

# returns the length of word
def l(word: str):
    total = 0
    for letter in word:
        total = total + 1
    return total

# returns the number of (capital or lower case) A's in word
def a(word: str):
    total = 0
    for letter in word:
        if letter == 'a' or letter == 'A':
            total = total + 1
    return total

# returns the number of consonants in word minus the number of vowels in word
def v(word: str):
    total = 0
    for letter in word:
        if letter in 'aeiouAEIOU':
            total = total - 1
        if letter not in 'aeiouAEIOU':
            total = total + 1
    return total

# f builds a list of the numbers 0 to n-1 and sends that list to the function s
# f returns the square root of the output of s(lst)
def f(n: int):
    lst = []
    for i in range(n):
        lst.append(i)
    result = s(lst)
    return math.sqrt(result)

# s outputs the sum of all the elements in new_lst
def s(new_lst: list):
    total = 0
    for i in new_lst:
        total = total + i
    return total

# d counts how many times you need to divide num by 2 until you get a number less than 1
# if you have seen logarithms in math before, how is this similar to log base 2?
def d(num: float):
    count = 0
    while num > 1:
        num = num/2
        count = count + 1
    return count
