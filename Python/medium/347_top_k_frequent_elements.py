from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1

        return sorted(counts, key=counts.get, reverse=True)[:k]
