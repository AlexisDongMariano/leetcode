# ==============================
#         Information
# ==============================

# Title: 1720 - Decode XORed Array
# Link: https://leetcode.com/problems/decode-xored-array/
# Difficulty: Easy
# Language: Python

# Problem:
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Example
    # Input: s = "RLRRLLRLRL"
    # Output: 4
    # Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# ==============================
#         Solution
# ==============================


def balanced_string_split(s):
    l = r = output = 0

    for char in s:
        if char.upper() == 'L':
            l += 1
        else:
            r += 1

        if l == r:
            output += 1
            l = r = 0
        
    
    return output


def balanced_string_split2(s):
    balance = counter = 0

    for char in s:
        if char == 'L':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            counter += 1
    
    return counter



s1 = "RLRRLLRLRL"
s2 = "RLLLLRRRLR"
s3 = "LLLLRRRR"
s4 = "RLRRRLLRLL"


print(balanced_string_split(s1))
print(balanced_string_split(s2))
print(balanced_string_split(s3))
print(balanced_string_split(s4))

print(balanced_string_split2(s1))
print(balanced_string_split2(s2))
print(balanced_string_split2(s3))
print(balanced_string_split2(s4))
