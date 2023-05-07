from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1



# arr = [0,0,1,1,1,2,2,3,3,4]
arr = [1, 1]
s = Solution()
print(s.removeDuplicates(arr))
print(arr)
