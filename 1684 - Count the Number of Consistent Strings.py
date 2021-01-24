# ==============================
#         Information
# ==============================

# Title: 1684 - Count the Number of Consistent Strings
# Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/
# Difficulty: Easy
# Language: Python

# Problem:
# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

# Example
    # Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    # Output: 2
    # Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# ==============================
#         Solution
# ==============================


# 0(m * n)
def count_consistent_strings(allowed, words):
    allowed_map = {i:i for i in allowed}
    counter = 0
    
    for word in words:
        with_other_char = True
        for char in word:
            if char not in allowed_map:
                with_other_char = False
        if with_other_char:
            counter += 1
    
    return counter


# 0(n) time complexity
def count_consistent_strings2(allowed, words):
    counter = 0
    allowed_set = set(allowed)
    words_map = {}
    x = 0

    for word in words:
        if word not in words_map.keys():
            words_map[word] = set(word)
        else:
            words_map[word + str(x)] = set(word)
            x += 1

    for key, value in words_map.items():
        words_map[key] = value.difference(allowed_set)

    for value in words_map.values():
        if not value:
            counter += 1
    
    return counter


def count_consistent_strings3(allowed, words):
    counter = 0
    allowed_set = set(allowed)

    for word in words:
        if not set(word).difference(allowed_set):
            counter += 1
    
    return counter


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]
allowed3 = "cad"
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]
allowed4 = "exdohslrwipnt"
words4 = ["xrwlstne","rs","ioetdll","lwi","r","pieonois","r","xtp","stia","gicfuvmnr","hdntpxse","sodxws","v","hstirooon","d"]

print(count_consistent_strings(allowed, words))
print(count_consistent_strings(allowed2, words2))
print(count_consistent_strings(allowed3, words3))
print(count_consistent_strings(allowed4, words4))
print(count_consistent_strings2(allowed, words))
print(count_consistent_strings2(allowed2, words2))
print(count_consistent_strings2(allowed3, words3))
print(count_consistent_strings2(allowed4, words4))
print(count_consistent_strings3(allowed, words))
print(count_consistent_strings3(allowed2, words2))
print(count_consistent_strings3(allowed3, words3))
print(count_consistent_strings3(allowed4, words4))
