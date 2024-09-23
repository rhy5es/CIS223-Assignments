"""
create function "fantabulous_sort" that uses an insertion sort of the # of elements is less than or equal to 10, and a quick sort if the # of elements is greater than 10
"""

def fantabulous_sort(num_list):
    if len(num_list) <= 10:
        return insert_sort(num_list)
    else:
        return quick_sort(num_list)
    
def insert_sort(num_list): #this is the same insertion sort from question #1 (4a), minus the inversion counter part
    for i in range(1, len(num_list)): 
        key = num_list[i] 
        j = i - 1 
        while j >= 0 and key < num_list[j]: 
            num_list[j+1] = num_list[j] 
            j -= 1
        num_list[j + 1] = key
    return num_list

def quick_sort(num_list): #this is the same quick sort from question #7 (4e)
    if len(num_list) <= 10:
        return insert_sort(num_list) #this line is not in 4e, just added to streamline things a bit
    
    num1 = num_list[0]
    num2 = num_list[len(num_list) // 2]
    num3 = num_list[len(num_list) - 1]
    if num2 <= num1 <= num3 or num3 <= num1 <= num2:
        pivot = num1
    elif num1 <= num2 <= num3 or num3 <= num2 <= num1:
        pivot = num2
    else:
        pivot = num3

    less = []
    equal = []
    greater = []
    for i in range(len(num_list)):
        if num_list[i] < pivot:
            less.append(num_list[i])
        elif num_list[i] > pivot:
            greater.append(num_list[i])
        else:
            equal.append(num_list[i])
    return quick_sort(less) + equal + quick_sort(greater)