from math import ceil


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        values = [int(i) for i in str(x)]
        print(values)
        for (i, value) in enumerate(values):
            print(i, value)
            if value != values[len(values) - i - 1]:
                return False

            if i > ceil(len(values) / 2):
                break


        return True
