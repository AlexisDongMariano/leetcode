# ==============================
#         Information
# ==============================

# Title: 942 - DI String Match
# Link: https://leetcode.com/problems/di-string-match/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a string S that only contains "I" (increase) or "D" (decrease),
# let N = S.length.

# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]

# Example
# Input: "IDID"
# Output: [0,4,1,3,2]

# Input: "III"
# Output: [0,1,2,3]

# ==============================
#         Solution
# ==============================


def di_string_match(input):
    lo = 0
    hi = len(input)
    output = []
    for i in input:
        if i.upper() == 'I':
            output.append(lo)
            lo += 1
        else:
            output.append(hi)
            hi -= 1
    output.append(hi)
    return output

input = 'IDID'
input2 = 'III'
print(di_string_match(input))
print(di_string_match(input2))
