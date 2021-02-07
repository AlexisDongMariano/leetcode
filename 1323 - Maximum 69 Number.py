# ==============================
#         Information
# ==============================

# Title: 1323 - Maximum 69 Number
# Link: https://leetcode.com/problems/maximum-69-number/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Example
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666. 
# The maximum number is 9969.

# ==============================
#         Solution
# ==============================


def max_69_num(nums):
    str_nums = [i for i in str(nums)]

    for i in range(len(str_nums)):
        if str_nums[i] == '6':
            str_nums[i] = '9'
            break

    return int(''.join(str_nums))


def max_69_num2(nums):
    return int(str(nums).replace('6', '9', 1))


input = 9669

print(max_69_num(input))
print(max_69_num2(input))
