# ==============================
#         Information
# ==============================

# Title: 1281 - Subtract the Product and Sum of Digits of an Integer
# Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# Example
    # Input: n = 234
    # Output: 15 
    # Explanation: 
    # Product of digits = 2 * 3 * 4 = 24 
    # Sum of digits = 2 + 3 + 4 = 9 
    # Result = 24 - 9 = 15

# ==============================
#         Solution
# ==============================

def subtract_product_and_sum(n):
    digits = [int(i) for i in str(n)]
    sum, product = 0, 1

    for i in digits:
        sum += i
        product *= i

    return product - sum  


n = 234
print(subtract_product_and_sum(n))

