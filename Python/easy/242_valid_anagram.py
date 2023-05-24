class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        values = {}
        for value in s:
            if value in values:
                values[value] += 1
            else:
                values[value] = 1

        for value in t:
            res = values.get(value)
            if not res:
                return False

            values[value] -= 1

        for key in values:
            if values[key] != 0:
                return False

        return True
