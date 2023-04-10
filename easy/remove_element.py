from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            else:
                nums[i] = 51

        return j


s = Solution()
assert s.removeElement([0,1,2,2,3,0,4,2], 2) == 5
