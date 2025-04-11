from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We return indexes
        #Only iterate over the list once for optimal performance O(n) time

        # Naive approach bc O(n^2) time 

        # Define an empty list to store indexes
        result = []

        # Iterave over the list of numbers twice so that we can check all combinations of numbers
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Check if the sum of the two numbers is equal to the target and that the indexes are not the same
                if ((nums[i] + nums[j]) == target) and (i != j) :
                    result.append(i)
                    result.append(j)
                    # Once found break out of the loop
                    break
            if result:
                break
        # Return the list of indexes
        return result