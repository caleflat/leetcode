from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = ['' for i in range(n)]
        offset = 0
        result = []
        mid = n // 2

        for i in range(mid):
            if ['(', ')'] in curr[i]:
                continue

            curr[i] = '('
            curr[i + offset] = ')'
            result.append(curr)

            offset += 1

        return result


s = Solution()
print(s.generateParenthesis(4))
