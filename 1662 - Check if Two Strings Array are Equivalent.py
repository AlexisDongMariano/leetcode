# ==============================
#         Information
# ==============================

# Title: 1662 - Check If Two String Arrays are Equivalent
# Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# Difficulty: Easy
# Language: Python

# Problem:
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

# Example
    # Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    # Output: true
    # Explanation:
    # word1 represents string "ab" + "c" -> "abc"
    # word2 represents string "a" + "bc" -> "abc"
    # The strings are the same, so return true.

# ==============================
#         Solution
# ==============================


def array_strings_are_equal(word1, word2):
    return ''.join(word1) == ''.join(word2)


word1 = ["ab", "c"]
word2 = ["a", "bc"]
word3 = ["a", "cb"]
word4 = ["ab", "c"]
word5  = ["abc", "d", "defg"]
word6 = ["abcddefg"]

print(array_strings_are_equal(word1, word2))
print(array_strings_are_equal(word3, word4))
print(array_strings_are_equal(word5, word6))

