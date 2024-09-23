"""
Takes amount of change to be given and list of ints (coin values) 
Returns a dict containing how many of each coin to provide change # with least amount of coins.
"""

def greedy_change(needed_total: int, denominations: list[int]):
    result_dict = {}
    denominations.reverse() #reverses denominations list so coin with greatest value is first
    return greedy_change_helper(needed_total, denominations, result_dict)

def greedy_change_helper(needed_total, denominations, result_dict): #so the result_dict is continuous with each iteration
    if needed_total <= 0: 
        return result_dict
    elif len(denominations) == 0: #checks if list is empty
        return result_dict
    else:
        coin = denominations[0]
        count = 0
        while needed_total >= coin: #while coin can stil be subtracted from needed_total
            needed_total -= coin
            count += 1 
        result_dict.update({coin : count}) #adds to result_dict the value of coin and how many of those coins are needed
        return greedy_change_helper(needed_total, denominations[1:], result_dict)
    
print(greedy_change(35, [3, 7, 8, 12]))
print(greedy_change(35, [5, 7, 8, 25]))
