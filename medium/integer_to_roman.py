class Solution:
    def intToRoman(self, num: int) -> str:
        key = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        value = ["M", "CM", "D", "CD", "C", "XC",
                 "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        for i in range(len(key)):
            while num >= key[i]:
                roman += value[i]
                num -= key[i]

        return roman
