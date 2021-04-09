# ==============================
#         Information
# ==============================

# Title: 1002 - Find Common Characters
# Link: https://leetcode.com/problems/find-common-characters/
# Difficulty: Easy
# Language: Python

# Problem:
# Given an array A of strings made only from lowercase letters, return a list 
# of all characters that show up in all strings within the list (including
# duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final
# answer.

# You may return the answer in any order.

# Example
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]

# ==============================
#         Solution
# ==============================


# 0(n*m)
def common_chars(input):
    word1 = list(input[0])
    for word in input[1:]:
        check_word = []
        for c in word:
            if c in word1:
                check_word.append(c)
                word1.remove(c)
        word1 = check_word
    return word1


input = ['bella','label','roller']
print(common_chars(input))