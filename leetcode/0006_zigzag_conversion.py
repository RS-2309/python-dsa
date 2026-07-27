class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        nestList = ["" for _ in range(numRows)]
        index = 0
        typeInc = 0

        for i in s:
            nestList[index] += i
            if typeInc == 0:
                index += 1
            else:
                index -= 1

            if index >= numRows:
                index -= 2
                typeInc = 1
            elif index <= 0:
                typeInc = 0
        
        res = ""

        for string in nestList:
            res += string

        return res