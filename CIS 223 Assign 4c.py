"""
create a class, "person," which includes a name and an age. 
then use selection sort to sort a list of people
"""

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person({self.name}, {self.age})'

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    
def select_sort_people_by_age(lyst):
    for i in range(len(lyst) - 1):
        min_index = i
        for j in range(i+1, len(lyst)):
            if lyst[j].get_age() < lyst[min_index].get_age():
                min_index = j
        (lyst[i].get_age()), (lyst[min_index].get_age()) == (lyst[min_index].get_age()), (lyst[i].get_age())
    return lyst
