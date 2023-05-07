class Solution:
    def reverse(self, x: int) -> int:
        lim = 2**31

        sign = 1
        if x < 0:
            x = -x
            sign = -1

        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10

        if rev > lim - 1:
            return 0

        return rev * sign


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
