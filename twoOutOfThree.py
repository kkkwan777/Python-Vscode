from typing import List
from collections import defaultdict

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set_before_list = set()

        for x in nums2:
            if x in nums1:
                set_before_list.add(x)

        for x in nums3:
            if x in nums1 or x in nums2:
                set_before_list.add(x)

        return list(set_before_list)

nums1 = [2,15,10,11,14,12,14,11,9,1]
nums2 = [8,9,13,2,11,8]
nums3 = [13,5,15,7,12,7,8,3,13,15]
Kwan = Solution()
print(Kwan.twoOutOfThree(nums1, nums2, nums3))
