# ==============================
#         Information
# ==============================

# Title: 709 - To Lower Case
# Link: https://leetcode.com/problems/to-lower-case/
# Difficulty: Easy
# Language: Python

# Problem:
# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example
# Input: "Hello"
# Output: "hello"

# ==============================
#         Solution
# ==============================

def to_lower_case(input):
    if not input:
        return None

    output = ''

    for c in input:
        if 65 <= ord(c) <= 90:
            output += chr(ord(c)+32)
        else:
            output += c
    
    return output


def to_lower_case2(input):
    if not input:
        return None
        
    return ''.join([chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in input])



input = 'Hello'
input2 = ''

print(to_lower_case(input))
print(to_lower_case(input2))

print(to_lower_case2(input))
print(to_lower_case2(input2))



