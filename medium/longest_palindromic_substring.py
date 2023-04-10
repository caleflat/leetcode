class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)

        if n == 0:
            return ""

        if n == 1:
            return s

        dp = [[False for _ in range(n)] for _ in range(n)]
        longest = ""

        # all substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
            longest = s[i]

        # check for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                longest = s[i:i+2]

        # check for substrings of length greater than 2
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if k > len(longest):
                        longest = s[i:j+1]

        return longest
