from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, num in enumerate(nums):
            remainder = target - num
            if remainder in values:
                return [values[remainder], idx]

            values[num] = idx

        return [-1, -1]


