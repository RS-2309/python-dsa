from recursion import *

print("========== RECURSION TEST ==========\n")

# -------------------------------
# Basic Recursion
# -------------------------------
print("Countdown:")
countdown(5)
print()

print("Countup:")
countup(5)
print()

print("Sum to N")
print("sum_to_n(10):", sum_to_n(10))
print()

print("Factorial")
print("factorial(5):", factorial(5))
print()

# -------------------------------
# String Recursion
# -------------------------------
print("Reverse String")
print("Original: Hello World")
print("Reversed:", end=" ")
reverse_string("Hello World")
print()

print("Palindrome")
print("'racecar':", is_palindrome("racecar"))
print("'A man a plan a canal Panama':", is_palindrome("A man a plan a canal Panama"))
print("'python':", is_palindrome("python"))
print()

# -------------------------------
# List Recursion
# -------------------------------
numbers = [7, 2, 5, 10, 8, 10]

print("List:", numbers)
print("Recursive Sum:", recursive_sum(numbers))
print("Recursive Max:", recursive_max(numbers))
print("Occurrences of 10:", count_occurrences(numbers, 10))
print("Occurrences of 100:", count_occurrences(numbers, 100))
print()

# -------------------------------
# Binary Search
# -------------------------------
sorted_numbers = [2, 5, 7, 10, 15, 21, 30, 42]

print("Binary Search")
print("Array:", sorted_numbers)
print("Find 15:", binary_search(sorted_numbers, 15))
print("Find 42:", binary_search(sorted_numbers, 42))
print()

# -------------------------------
# Classic Problems
# -------------------------------
print("Fibonacci")
print("fibonacci(10):", fibonacci(10))
print()

print("Power")
print("2^10 =", power(2, 10))
print("5^3 =", power(5, 3))
print()

print("Greatest Common Divisor")
print("gcd(48, 18):", gcd(48, 18))
print("gcd(84, 30):", gcd(84, 30))
print()

print("========== TEST COMPLETE ==========")