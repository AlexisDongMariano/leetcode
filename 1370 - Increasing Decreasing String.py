# ==============================
#         Information
# ==============================

# Title: 1370 - Increasing Decreasing String
# Link: https://leetcode.com/problems/increasing-decreasing-string/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a string s. You should re-order the string using the following algorithm:
#
# 1. Pick the smallest character from s and append it to the result.
# 2. Pick the smallest character from s which is greater than the last appended
# character to the result and append it.
# 3. Repeat step 2 until you cannot pick more characters.
# 4. Pick the largest character from s and append it to the result.
# 5. Pick the largest character from s which is smaller than the last appended
# character to the result and append it.
# 6. Repeat step 5 until you cannot pick more characters.
# 7. Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once
# you can choose any occurrence and append it to the result.
# Return the result string after sorting s with this algorithm.

# Example:
# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

# ==============================
#         Solution
# ==============================


def fill_output(order, char_map, output):
    for i in order:
        if i in char_map:
            output.append(i)
            char_map[i] -= 1

            if char_map[i] == 0:
                del char_map[i]

    return output


def sort_string(s):
    char_set = set(s)
    increasing = sorted(char_set)
    decreasing = sorted(char_set, reverse=True)
    output = []
    
    # create dictionary with unique chars as key and occurrence as value
    char_map = {}
    for c in s:
        if c in char_map:
            char_map[c] += 1
        else:
            char_map[c] = 1
    
    # build the output based on the given logic
    while char_map:
        output = fill_output(increasing, char_map, output)
        output = fill_output(decreasing, char_map, output)

    return ''.join(output)


s = 'aaaabbbbcccc'

print(sort_string(s))

