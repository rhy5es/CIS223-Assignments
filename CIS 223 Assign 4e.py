"""
create a quick sort that picks the median of three randomly selected elems as the pivot
"""

def quick_sort_random_median_pivot(lyst): #using the unoptimized version because that makes more sense in my head
    if len(lyst) <= 1:
        return lyst
    
    #i'm sure there's a simpler way of doing this, but this is what I have
    num1 = lyst[0]
    num2 = lyst[len(lyst) // 2]
    num3 = lyst[len(lyst) - 1]
    if num2 <= num1 <= num3 or num3 <= num1 <= num2:
        pivot = num1
    elif num1 <= num2 <= num3 or num3 <= num2 <= num1:
        pivot = num2
    else:
        pivot = num3

    less = []
    equal = []
    greater = []
    for i in range(len(lyst)):
        if lyst[i] < pivot:
            less.append(lyst[i])
        elif lyst[i] > pivot:
            greater.append(lyst[i])
        else:
            equal.append(lyst[i])
    return quick_sort_random_median_pivot(less) + equal + quick_sort_random_median_pivot(greater)