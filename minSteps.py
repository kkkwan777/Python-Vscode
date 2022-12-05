from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        num_of_steps = 0
        list1 = [x for x in s]
        list2 = [y for y in t]

        print(len(list1), "and", list1)
        print(len(list2), "and", list2)
        return num_of_steps

kwan = Solution()
print(kwan.minSteps("leetcode", "practice"))