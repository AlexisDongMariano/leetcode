# ==============================
#         Information
# ==============================

# Title: 1051 - Height Checker
# Link: https://leetcode.com/problems/height-checker/
# Difficulty: Easy
# Language: Python

# Problem:
# Students are asked to stand in non-decreasing order of heights for an annual
# photo.

# Return the minimum number of students that must move in order for all students
# to be standing in non-decreasing order of height.

# Notice that when a group of students is selected they can reorder in any
# possible way between themselves and the non selected students remain on their
# seats.

# Example:
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# Current array : [1,1,4,2,1,3]
# Target array  : [1,1,1,2,3,4]
# On index 2 (0-based) we have 4 vs 1 so we have to move this student.
# On index 4 (0-based) we have 1 vs 3 so we have to move this student.
# On index 5 (0-based) we have 3 vs 4 so we have to move this student.

# ==============================
#         Solution
# ==============================


# time complexity depends on the sorted()
def height_checher(heights):
    sorted_heights = sorted(heights)
    output = 0
    for i in range(len(sorted_heights)):
        if heights[i] != sorted_heights[i]:
            output += 1
    return output


# same as above but one-liner
def height_checker2(heights):
    return len([x for x in range(len(heights)) if heights[x] != sorted(heights)[x]])


#  return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


heights = [1,1,4,2,1,3]
heights2 = [5,1,2,3,4]
heights3 = [1,2,3,4,5]
print(height_checher(heights))
print(height_checher(heights2))
print(height_checher(heights3))

print(height_checker2(heights))
print(height_checker2(heights2))
print(height_checker2(heights3))

