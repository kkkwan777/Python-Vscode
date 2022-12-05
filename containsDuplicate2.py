from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_duplicate = False

        set_nums = set(nums)
        if len(set_nums) != len(nums):
            check_duplicate = True
        return check_duplicate
