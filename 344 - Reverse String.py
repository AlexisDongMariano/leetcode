# ==============================
#         Information
# ==============================

# Title: 344 - Reverse String
# Link: https://leetcode.com/problems/reverse-string/
# Difficulty: Easy
# Language: Python

# Problem:
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# Example
    # Input: ["h","e","l","l","o"]
    # Output: ["o","l","l","e","h"]

# ==============================
#         Solution
# ==============================

def reverse_string(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    length = len(s)

    for i in range(len(s)//2):
        r = (length - 1) - i
        s[i], s[r] = s[r], s[i]
    
    print(s)


def reverse_string2(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s = s[::-1] # slicing method
    print(s)


def reverse_string3(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s = [c for c in ''.join(reversed(s))]
    print(s)


def reverse_string4(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()
    print(s)


s = ['h', 'e', 'l', 'l', 'o']
s2 = ['h', 'e', 'l', 'l', 'o']
s3 = ['h', 'e', 'l', 'l', 'o']
s4 = ['h', 'e', 'l', 'l', 'o']

reverse_string(s)
reverse_string2(s2)
reverse_string3(s3)
reverse_string4(s4)




