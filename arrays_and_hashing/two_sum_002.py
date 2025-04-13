from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(n)

        # First, declare a hashMap/dictionary to store the values and their indices
        hashMap = {}
        
        # Then, iterate through nums and calculate the complement of each number
        # Then, check if the complement is already in the hashMap
        # If it is, return the indices of the complement and the current number
        # Else, add the current number and its index to the hashMap
        # Finally, return an empty list if no solution is found
        for i in range(len(nums)):
            complement = target - nums[i] #4
            if complement in hashMap:
                return [hashMap[complement], i]
            else:
                hashMap[nums[i]] = i
        return []