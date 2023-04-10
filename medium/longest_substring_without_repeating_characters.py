class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            if c in found and start <= found[c]:
                start = found[c] + 1
            else:
                max_len = max(max_len, i - start + 1)
            found[c] = i

        return max_len
