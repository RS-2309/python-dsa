class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        data = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        if len(digits) == 1:
            return data[digits[0]]

        elif len(digits) == 2:
            result = []

            for l1 in data[digits[0]]:
                for l2 in data[digits[1]]:
                    result.append(l1 + l2)

            return result

        elif len(digits) == 3:
            result = []

            for l1 in data[digits[0]]:
                for l2 in data[digits[1]]:
                    for l3 in data[digits[2]]:
                        result.append(l1 + l2 + l3)

            return result

        else:
            result = []

            for l1 in data[digits[0]]:
                for l2 in data[digits[1]]:
                    for l3 in data[digits[2]]:
                        for l4 in data[digits[3]]:
                            result.append(l1 + l2 + l3 + l4)

            return result