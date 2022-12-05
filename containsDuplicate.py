from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_duplicate = False

        #create a dictionary
        dictionary = {}

        #create key for each item in the list
        for x in range(len(nums)):
            dictionary[nums[x]] = 0

        #store a default value [1] for each key in the dictionary 
        for x in range(len(nums)):
            dictionary[nums[x]] += 1

        #check whether the value repeated in the list
        for key in dictionary:
            print(key, dictionary[key])
            if dictionary[key] > 1:
                check_duplicate = True

        return check_duplicate

nums = [1, 2, 3, 2]

leetcode_solution1 = Solution()
print(nums, leetcode_solution1.containsDuplicate(nums))
