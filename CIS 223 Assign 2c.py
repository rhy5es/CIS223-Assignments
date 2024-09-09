"""
with a sequence of n distinct integers listed in increasing order, find two integers that have a difference of k with a recursive function
"""
   
def findDifference(s: list[int], k: int): #ex: s = [2, 7, 9, 12, 25], k = 2
    return findDifferenceHelper(s, k, 0) #should return (7, 9)

def findDifferenceHelper(s: list[int], k: int, pointer: int):
    if pointer >= len(s): 
        return None
    else:
        for number in s: #tests one number at a time
            print(number)
            if s[pointer] - k == number: #ex: 2 - 2 = 0, 0 != 2, move to else statement
                return number, s[pointer]
            else:
                continue #continue on to next number. ex: 0 != 7, 0 != 9, etc etc
        return findDifferenceHelper(s, k, pointer + 1)
