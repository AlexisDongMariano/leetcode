# ==============================
#         Information
# ==============================

# Title: 412 - Fizz Buzz
# Link: https://leetcode.com/problems/fizz-buzz/
# Difficulty: Easy
# Language: Python

# Problem:
# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for
# the multiples of five output “Buzz”. For numbers which are multiples of both three
# and five output “FizzBuzz”.


# Example
# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

# ==============================
#         Solution
# ==============================

def fizzbuzz(n):
    output = []

    for i in range(1, n + 1):
        div_by_3 = i % 3 == 0
        div_by_5 = i % 5 == 0

        if div_by_3 and div_by_5:
            output.append('FizzBuzz')
        elif div_by_3:
            output.append('Fizz')
        elif div_by_5:
            output.append('Buzz')
        else:
            output.append(str(i))
    
    return output


def fizzbuzz2(n):
    output = []
    div3 = div5 = 0

    for i in range(1, n + 1):
        div3 += 1
        div5 += 1

        if div3 == 3 and div5 == 5:
            output.append('FizzBuzz')
            div3 = div5 = 0
        elif div3 == 3:
            output.append('Fizz')
            div3 = 0
        elif div5 == 5:
            output.append('Buzz')
            div5 = 0
        else:
            output.append(str(i))
        
    return output


n = 15

print(fizzbuzz(n))
print(fizzbuzz2(n))



