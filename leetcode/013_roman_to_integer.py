class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0

        values = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        i = 0

        for value, symbol in values:
            while s[i:i+2 if i + 2 <= len(s) else i] == symbol or s[i] == symbol:
                res += value
                i += 1 if len(symbol) == 1 else 2
                if i >= len(s):
                    break
            if i >= len(s):
                break

        return res