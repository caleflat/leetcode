key = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        values = [c for c in s]
        skip_next = False
        sum = 0
        for (i, value) in enumerate(values):
            if skip_next:
                skip_next = False
                continue

            if i == len(values) - 1:
                sum += key[value]
                continue

            skip_next = True
            if value == "I" and values[i + 1] == "V":
                sum += 4
            elif value == "I" and values[i + 1] == "X":
                sum += 9
            elif value == "X" and values[i + 1] == "L":
                sum += 40
            elif value == "X" and values[i + 1] == "C":
                sum += 90
            elif value == "C" and values[i + 1] == "D":
                sum += 400
            elif value == "C" and values[i + 1] == "M":
                sum += 900
            else:
                sum += key[value]
                skip_next = False


        return sum

