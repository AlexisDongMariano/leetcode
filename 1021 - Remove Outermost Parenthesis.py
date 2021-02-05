# ==============================
#         Information
# ==============================

# Title: 1021 - Remove Outermost Parenthesis
# Link: https://leetcode.com/problems/remove-outermost-parentheses/
# Difficulty: Easy
# Language: Python

# Problem:
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are
# valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()",
# and "(()(()))" are all valid parentheses strings.

# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way
# to split it into S = A+B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
# where P_i are primitive valid parentheses strings.

# Return S after removing the outermost parentheses of every primitive string in the primitive
# decomposition of S.

# Example
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# ==============================
#         Solution
# ==============================

# 0(n)
def remove_outer_parentheses(S):
    p_stack = []
    output = []
    
    for i, p in enumerate(S):
        if not p_stack:
            p_stack.append(p)
        elif len(p_stack) == 1 and p == ')':
            p_stack.pop()
        else:
            if p == '(':
                p_stack.append(p)
                output.append(p)
            else:
                p_stack.pop()
                output.append(p)
            
    return ''.join(output)


input = '(()())(())'

print(remove_outer_parentheses(input))
