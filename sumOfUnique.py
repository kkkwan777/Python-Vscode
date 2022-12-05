from typing import List
from collections import defaultdict
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sumbox = 0
        
        #create a dictionary
        dictionary = defaultdict(int)

        for x in nums:
            dictionary[x] += 1

        for key in dictionary:
            if dictionary[key] == 1:
                sumbox += key

        return sumbox
                
nums = [1, 2, 3, 2]
kwan = Solution()
print(kwan.sumOfUnique(nums))