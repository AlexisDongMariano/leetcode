# ==============================
#         Information
# ==============================

# Title: 1436 - Destination City
# Link: https://leetcode.com/problems/destination-city/
# Difficulty: Easy
# Language: Python

# Problem:
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists
# a direct path going from cityAi to cityBi. Return the destination city, that is, the
# city without any path outgoing to another city.
#
# It is guaranteed that the graph of paths forms a line without any loop, therefore,
# there will be exactly one destination city.

# Example:
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is
# the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

# ==============================
#         Solution
# ==============================


def destination_city(paths):
    departures = set(city[0] for city in paths)

    for path in paths:
        if path[1] not in departures:
            return path[1]


def destination_city2(paths):
    dic = {}
    for path in paths:
        for i, city in enumerate(path):
            if i == 0:
                dic[city] = dic.get(city, 0) + 1
            else:
                dic[city] = dic.get(city, 0) - 1
    
    for key in dic.keys():
        if dic[key] == -1:
            return key


def destination_city3(paths):
    departures = set(city[0] for city in paths)
    destination = set(city[1] for city in paths)

    return min(destination.difference(departures))


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

print(destination_city(paths))
print(destination_city2(paths))
print(destination_city3(paths))

