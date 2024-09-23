"""
find most common element in a list of numbers
"""
def most_common(lyst):
    counter1 = 0 #main counter outside loop, keeps track of highest num so far
    most_common_num = 0 #so we're able to return the actual number rather than the number of occurences
    for num1 in range(len(lyst)): #runtime of "for" loop: O(n)
        counter2 = 0 #internal counter, keeps track of current num1
        for num2 in range(len(lyst)): #runtime of "for" loop: O(n)
            if lyst[num1] == lyst[num2]:
                counter2 += 1
            if counter2 > counter1: #if the internal counter is larger, means that current num1 has more occurences
                counter1 = counter2 #external count is replaced with internal count
                most_common_num = lyst[num1] #current number with the most occurences is saved
            else:
                continue 
    return most_common_num #total runtime: O(n^2)



