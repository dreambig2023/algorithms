"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

"""

from typing import List


class RunningSum:

    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Calculate running sum 
        :param nums: List of integers - max length 1000
        :returns: List
        """

        length = len(nums)

        if length > 1000:

            raise ValueError("Length of num array should be 1 to 1000")

        new_list = list()

        for i in range(length):

            total = 0

            for j in nums[:i+1]:

                total = total + j

            new_list.append(total)

        return new_list

