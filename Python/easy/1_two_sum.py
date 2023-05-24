from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for (idx, num) in enumerate(nums):
            remainder = target - num
            rIdx = seen.get(remainder)
            if rIdx is None:
                seen[num] = idx
                continue

            return [rIdx, idx]


        return []

