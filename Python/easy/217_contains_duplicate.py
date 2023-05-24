from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for value in nums:
            curr = counts.get(value)
            if not curr:
                counts[value] = 1

            if curr == 2:
                return True

            counts[value] += 1

        return False
