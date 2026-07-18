# ===============================
# RECURSION
# ===============================

# -------------------------------
# Basic Recursion
# -------------------------------

def countdown(n):
    if n == 0:
        print(0)
        return
    print(n)
    countdown(n-1)


def countup(n):
    if n == 0:
        print(0)
        return
    countup(n-1)
    print(n)

def sum_to_n(n):
    if n-1 == 0:
        return 1
    return n + sum_to_n(n-1)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# -------------------------------
# String Recursion
# -------------------------------

def reverse_string(s):
    print(s[::-1])


def is_palindrome(s):
    if s.replace(" ", "").lower() == s[::-1].replace(" ", "").lower():
        return True
    return False


# -------------------------------
# List Recursion
# -------------------------------

def recursive_sum(nums, i = 0):
    if i == len(nums):
        return 0
    return nums[i] + recursive_sum(nums, i + 1)
    


def recursive_max(nums, i = 0):
    if i == len(nums):
        max = nums[-1]
        return max
    
    max = recursive_max(nums, i + 1)

    if max < nums[i]:
        max = nums[i]
        
    return max


def count_occurrences(nums, target, i = 0, count = 0):
    if nums[i] == target:
        count += 1

    if i + 1 == len(nums):
        return count
    
    count = count_occurrences(nums, target, i + 1, count)
    return count


# -------------------------------
# Searching
# -------------------------------

def binary_search(nums, target):
    if len(nums) == 0:
        return None
    index = len(nums)//2
    if nums[index] > target:
        return binary_search(nums[:index], target)
    if nums[index] < target:
        return binary_search(nums[index+1:], target) + index + 1
    if nums[index] == target:
        return index
    if index == 0:
        return None


# -------------------------------
# Classic Problems
# -------------------------------

def fibonacci(n, a = 0, b = 1):
    if n == 0:
        return a
    
    return fibonacci(n - 1, b, a + b)

def power(base, exponent):
    if exponent == 0:
        return 1
    
    return base*power(base, exponent - 1)

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)



# -------------------------------
# Backtracking (Later)
# -------------------------------

# Permutations
# N Queens
# Sudoku Solver

if __name__ == '__main__':
    countdown(10)
    print()
    countup(10)
    print()
    print(sum_to_n(10))
    print()
    print(factorial(10))
    print()
    reverse_string("Hello")
    print()
    print(is_palindrome("No Lemons No Melon"))
    print()
    print(is_palindrome("No Lemons No Oranges"))
    print()
    print(recursive_sum([1, 2, 3, 4, 5, 10]))
    print()
    print(recursive_max([1, 2, 3, 20, 4, 5, 10]))
    print()
    print(count_occurrences([11, 10, 5, 2, 3, 4, 3, 15, 11, 10, 5, 10, 9, 13, 11, 4, 15, 10, 11, 14, 8, 3, 10, 15, 4], 11))
    print()
    print(fibonacci(5))
    print()
    print(power(2, 10))