class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x_str = str(x)[::-1]
        else:
            x_str = "-" + str(-x)[::-1]
        
        if int(x_str) > 2**31 - 1 or int(x_str) < -2**31:
            return 0
        else:
            return int(x_str)