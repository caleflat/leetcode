from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        result = 0
        closest = pow(10, 4) + 1
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    if abs(target - (nums[i] + nums[l] + nums[r])) < closest:
                        closest = target - (nums[i] + nums[l] + nums[r])
                        result = nums[i] + nums[l] + nums[r]

                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1

                    while r > target and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return result
        

