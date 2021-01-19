# ==============================
#         Information
# ==============================

# Title: 1108 - Defanging an IP Address
# Link: https://leetcode.com/problems/defanging-an-ip-address/
# Difficulty: Easy
# Language: Python

# Problem:
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

# Example
    # Input:
    # address = "1.1.1.1"
    # Output:
    # "1[.]1[.]1[.]1"

# ==============================
#         Solution
# ==============================

# 0(n) time complexity
# 0(n) space complexity, created new string and replaced in every n character
def defang_ip_address(address):
    defanged_ip = ''

    for i in address:
        if i == '.':
            defanged_ip += '[.]'
        else:
            defanged_ip += i

    return defanged_ip

# 0(n) time complexity maybe, have to check the python documentation
# simplest and cleanest
def defang_ip_address2(address):
    return address.replace('.', '[.]')


# another way of simple implementation using string manipulation functions
def defang_ip_address3(address):
    defanged_address = address.split('.')
    return '[.]'.join(defanged_address)


address = '1.1.1.1'

print(defang_ip_address(address))
print(defang_ip_address2(address))
print(defang_ip_address3(address))
