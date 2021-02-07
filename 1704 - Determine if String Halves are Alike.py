# ==============================
#         Information
# ==============================

# Title: 1704 - Determine if String Halves Are Alike
# Link: https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/
# Difficulty: Easy
# Language: Python

# Problem:
# You are given a string s of even length. Split this string into two halves of equal lengths,
# and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels
# ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase
# and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

# Example
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

# ==============================
#         Solution
# ==============================

# A. split the input list into two halves of equal lengths
# B. loop through the elements of the two lists
# C. if element/item in list a is vowel, store it in a variable
# D. do the same step in C for list b
# E. if the vowel count of list a and vowel count of list b are equal,
# return True, else, False

def halves_are_alike(s):
    vowel_map = set('aeiouAEIOU')   
    n = len(s) // 2
    a = s[:n]
    b = s[n:]
    a_vowel_count = b_vowel_count = 0
    
    for i in range(n):
        if a[i] in vowel_map:
            a_vowel_count += 1
        if b[i] in vowel_map:
            b_vowel_count += 1
    
    return a_vowel_count == b_vowel_count


input = 'book'

print(halves_are_alike(input))
