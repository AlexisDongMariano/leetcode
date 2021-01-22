# ==============================
#         Information
# ==============================

# Title: 1528 - Shuffle String
# Link: https://leetcode.com/problems/shuffle-string/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

# Example
    # Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
    # Output: "leetcode"
    # Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

# ==============================
#         Solution
# ==============================


# 0(n)
# generate a dictionary of index:character then recreate a new list
def restore_string(s, indices):
    char_index_map = dict(zip(indices, s))
    restored = ''

    for i in range(len(char_index_map)):
        restored += char_index_map[i]

    return restored


# 0(n) time complexity
# generate a new list with characters and the index of each is based on the values of another list
def restore_string2(s, indices):
    s_indices = [None] * len(s)

    j = 0
    for i in indices:
        s_indices[i] = s[j]
        j += 1

    return ''.join(s_indices)


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

s1 = "aaiougrt"
indices1 = [4,0,2,6,7,3,1,5]

print(restore_string(s, indices))
print(restore_string2(s, indices))
print(restore_string(s1, indices1))
print(restore_string2(s1, indices1))

