class Solution:
    def maxProduct(self, n: int) -> int:
        smaller = 0
        bigger = 0

        while n > 0:
            val = n % 10
            if val > bigger:
                smaller = bigger
                bigger = val
            elif val > smaller:
                smaller = val
            
            n //= 10

        return smaller*bigger