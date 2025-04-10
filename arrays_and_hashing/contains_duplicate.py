from typing import List

class Solution:
    '''
    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
    Ex:
    Input: nums = [1, 2, 3, 3]
    Output: true
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## Using a set to track seen numbers
        ## If a number is already in the set, return True
        hashMap = set()
        for item in nums:
            if item in hashMap:
                return True
            hashMap.add(item)
        return False