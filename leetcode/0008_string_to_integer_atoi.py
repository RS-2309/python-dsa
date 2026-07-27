class Solution:
    def myAtoi(self, s: str) -> int:
        refined = ""
        for i in s:
            if refined == "" and i == " ":
                refined += ""
            elif refined == "" and (i == "-" or i == "+"):
                refined += i
            elif "0" <= i <= "9":
                refined += i
            else:
                break
        if refined == "":
            refined += "0"
        
        integer = int(refined) if refined != "+" and refined != "-" else 0

        if integer > 2**31 - 1:
            integer = 2**31 - 1
        elif integer < -2**31:
            integer = -2**31

        return integer