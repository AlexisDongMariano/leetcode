# ==============================
#         Information
# ==============================

# Title: 1470 - Shuffle the Array
# Link: https://leetcode.com/problems/shuffle-the-array/submissions/
# Difficulty: Easy
# Language: Python

# Problem:
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Example
    # Input: accounts = [[1,2,3],[3,2,1]]
    # Output: 6
    # Explanation:
    # 1st customer has wealth = 1 + 2 + 3 = 6
    # 2nd customer has wealth = 3 + 2 + 1 = 6
    # Both customers are considered the richest with a wealth of 6 each, so return 6.

# ==============================
#         Solution
# ==============================

# 0(n^2) since we run sum() in every account which is list of wealth for every bank
def get_richest_account(accounts):
    return max([sum(account) for account in accounts])

    # above is equivalent of:
    # for account in accounts:
    #     wealth_list.append(sum(account))
    # return max(wealth_list)


# another implementation
def get_richest_account2(accounts):
    richest_amout = 0

    for i in accounts:
        account_sum = sum(i)
        if account_sum > richest_amout:
            richest_amout = account_sum
    
    return richest_amout


accounts = [[1,2,3],[3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]

print(get_richest_account(accounts))
print(get_richest_account(accounts2))
print(get_richest_account2(accounts2))