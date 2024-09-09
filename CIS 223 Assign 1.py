"""
input sequence "s" with at least 5 pos ints, return 5 largest ints
"""

#if "s" is a list, sorted() will work. if not, idfk
def largestFive(s):
    s = sorted(s, reverse = True)
    return s[0:5]
    

s = [2, 3, 18, 29, 4, 3, 100, 9, 15, 12]
print(largestFive(s))