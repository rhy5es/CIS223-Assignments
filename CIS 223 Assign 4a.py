"""
write an insertion sort. take in a list of numbers, return total amount of inversions
"""

def insert_sort(lyst): #sorts in-place
    insert_counter = 0 #counts number of inversions
    for i in range(1, len(lyst)): #i denotes current element
        key = lyst[i] #the element we're currenting looking at
        j = i - 1 #denotes the index of the "sorted" element
        while j >= 0 and key < lyst[j]: #while the index j is less than zero and the current element is greater than the "sorted" element
            lyst[j+1] = lyst[j] #the nearest unsorted element is replaced by the "sorted" element
            j -= 1
            insert_counter += 1
        lyst[j + 1] = key #moves on to the next element in the list
    return insert_counter
