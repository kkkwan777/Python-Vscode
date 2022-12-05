from typing import List
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_Anagram = True
        dict = defaultdict(int)
        for x in s:
            dict[x] += 1
        for y in t:
            dict[y] -= 1
        for key in dict:
            if dict[key] != 0:
                is_Anagram = False

        return is_Anagram

s = "abcbb"
t = "cbab"


kwan = Solution()
print(kwan.isAnagram(s, t))