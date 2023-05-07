opposites = { "}": "{", "]": "[", ")": "(" }


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        values = [c for c in s]
        previous = []
        for value in values:
            if value in ")}]":
                if len(previous) == 0:
                    return False

                if opposites[value] != previous.pop():
                    return False
            else:
                previous.append(value)

        
        return len(previous) == 0


s = Solution()
print(s.isValid("(({{}}))"))
