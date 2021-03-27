# ==============================
#         Information
# ==============================

# Title: 577 - Reverse Words in a String III
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.

# Example
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# ==============================
#         Solution
# ==============================

# 0(m * n)
def reverse_words(s):
    s_list = s.split(' ')
    output = []
    for s in s_list:
        r = s[::-1]
        print(r)
        output.append(r)
    return ' '.join(output)


# shortened version of above
def reverse_words2(s):
    return ' '.join([w[::-1] for w in s.split()])


s = "Let's take LeetCode contest"
print(reverse_words(s))
print(reverse_words2(s))