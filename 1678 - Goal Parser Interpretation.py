# ==============================
#         Information
# ==============================

# Title: 1678 - Goal Parser Interpretation
# Link: https://leetcode.com/problems/goal-parser-interpretation/
# Difficulty: Easy
# Language: Python

# Problem:
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of
#  "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()"
# as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated
# in the original order.
# Given the string command, return the Goal Parser's interpretation of command.

# Example
    # Input: command = "G()(al)"
    # Output: "Goal"
    # Explanation: The Goal Parser interprets the command as follows:
    # G -> G
    # () -> o
    # (al) -> al
    # The final concatenated result is "Goal".

# ==============================
#         Solution
# ==============================


def parse_goal(command):
    return command.replace('()', 'o').replace('(al)', 'al')


command = 'G()()()()(al)'
command2 = '(al)G(al)()()G'

print(parse_goal(command))
print(parse_goal(command2))