# ==============================
#         Information
# ==============================

# Title: 1252 - Cells with Odd Values in a Matrix
# Link: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
# Difficulty: Easy
# Language: Python

# Problem:
# Given n and m which are the dimensions of a matrix initialized by zeros and given an
# array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment
# all cells in row ri and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment
# to all indices.

# Example
# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

# ==============================
#         Solution
# ==============================
def odd_cells(n, m, indices):
    matrix = [[0 for i in range(m)] for i in range(n)]
    row = [r[0] for r in indices]
    col = [c[1] for c in indices]
    odd_count = 0

    for r in row:
        for i in range(m):
            matrix[r][i] += 1

    for c in col:
        for i in range(n):
            matrix[i][c] += 1
    
    for row in range(n):
        for col in range(m):
            if matrix[row][col] % 2 != 0:
                odd_count += 1
    
    return odd_count


n = 2
m = 3
indices = [[0,1],[1,1]]

print(odd_cells(n, m, indices))



