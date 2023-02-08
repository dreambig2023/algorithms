"""
Single numbers: 
    - Given an array of numbers num, all but one number in the list will be repeated twice. 
    Ex: [4, 2, 1, 2, 4]
    - Find the number unrepeated
Expend this further: 
    - Given an array of numbers, find the least number of repeated number. 
    Ex: [4, 4, 4, 2, 2, 1, 1, 1]
    - number 2 was repeated the least number of times. 
"""
from typing import List


class NumberArrays:
    def __init__(self, num: List):
        """Initialize the array of numbers"""
        if len(num) > 100:
            raise Exception.ValueError("Length of array cannot be over 100")
        self.num = num
    
    def get_single_number(self):
        """
        Get the single number in the array
        :returns int
        """
        count = {}
        for i in self.num:
            if i not in count.keys():
                count.update({i : 1})
            else:
                count.update({i : 2})
        for key, val in count.items():
            if val == 1:
                return key

    def get_least_repeated_number(self):
        """
        Get the least repeated number from the list
        :returns int
        """
        count = {}
        for i in self.num:
            if i in count.keys():
                count[i] = count[i] + 1
            else:
                count.update({i : 1})
        
        prev_val = 100
        out = {}
        for key, val in count.items():
            if val < prev_val:
                prev_val = val
                out = {key: val}
        return out


if __name__ == "__main__":
    array = NumberArrays([4,2,1,2,4])
    single_number = array.get_single_number()
    least_number = array.get_least_repeated_number()
    print(f"Single Num: {single_number}; Least Num: {least_number}")

    array = NumberArrays([4, 4, 2, 1, 1, 2,2, 4])
    least_number = array.get_least_repeated_number()
    print(f"Least Num: {least_number}")
