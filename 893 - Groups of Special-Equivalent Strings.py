# ==============================
#         Information
# ==============================

# Title: 650 - Robot Return to Origin
# Link: https://leetcode.com/problems/robot-return-to-origin/
# Difficulty: Easy
# Language: Python

# Problem:
# There is a robot starting at position (0, 0), the origin, on a 2D plane. 
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
# completes its moves.

# The move sequence is represented by a string, and the character moves[i]
# represents its ith move. Valid moves are R (right), L (left), U (up), and D
# (down). If the robot returns to the origin after it finishes all of its
# moves, return true. Otherwise, return false.

# Note: The way that the robot is "facing" is irrelevant. "R" will always make
# the robot move to the right once, "L" will always make it move left, etc.
# Also, assume that the magnitude of the robot's movement is the same for each
# move.

# Example
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the
# same magnitude, so it ended up at the origin where it started. Therefore, we
# return true.

# ==============================
#         Solution
# ==============================


# T: 0(n)
def robot_return(moves):
    h = 0
    v = 0

    for move in moves:
        move = move.upper()
        if move == 'L':
            h -= 1
        elif move == 'R':
            h += 1
        elif move == 'U':
            v += 1
        elif move == 'D':
            v -= 1
    
    if h == 0 and v == 0:
        return True
    return False


moves = "UD"
moves2 = "LL"
print(robot_return(moves))
print(robot_return(moves2))