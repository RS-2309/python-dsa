#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution: 
    def isPalindrome(self, x: int) -> bool: 
        return True if str(x) == str(x)[::-1] else False

'''Follow up: Could you solve it without converting the integer to a string?'''
#Time Complexity: O(log n)
#Space Complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x < 10:
            return True

        if -10 < x < 0:
            return False

        divisor = 1

        while x // divisor >= 10:
            divisor *= 10

        while x != 0:
            last = x % 10
            first = x // divisor

            if first != last:
                return False
            
            x = (x - first * divisor)//10
            divisor //= 100

            if divisor < 1:
                break
        
        return True