# ==============================
#         Information
# ==============================

# Title: 1450 - Number of Students Doing Homework at a Given Time
# Link: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
# Difficulty: Easy
# Language: Python

# Problem:
# Given two integer arrays startTime and endTime and given an integer queryTime.

# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

# Return the number of students doing their homework at time queryTime. More formally, return the number
# of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

# Example
# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1
# Explanation: We have 3 students where:
# The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at
# time 4.
# The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything
# at time 4.
# The third student started doing homework at time 3 and finished at time 7 and was the only student doing
# homework at time 4.

# ==============================
#         Solution
# ==============================

def busy_student(start_time, end_time, query_time):
    output = 0

    for i in range(len(start_time)):
        if start_time[i] <= query_time and end_time[i] >= query_time:
            output += 1

    return output



start_time = [1,2,3]
end_time = [3,2,7]
query_time = 4

start_time2 = [4]
end_time2 = [4]
query_time2 = 4

start_time3 = [4]
end_time3 = [4]
query_time3 = 5

print(busy_student(start_time, end_time, query_time))
print(busy_student(start_time2, end_time2, query_time2))
print(busy_student(start_time3, end_time3, query_time3))