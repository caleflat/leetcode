class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1

            if haystack[i:i + len(needle)] == needle:
                return i

        return -1

