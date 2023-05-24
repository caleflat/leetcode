from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {}
        for str in strs:
            chars = [x for x in str]
            chars.sort()
            key = "".join(chars)
            if key in values:
                values[key].append(str)
            else:
                values[key] = [str]

        return list(values.values())


s = Solution()
arr = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(arr)
