"""
Write a function, timeToRot, which takes in a grid of numbers, each of which is one of the following three values:

A 0 represents an empty spot;
A 1 represents a fresh orange;
A 2 represents a rotten orange.
Every minute, any fresh orange that is adjacent (up, down, left, right) to a rotten orange becomes rotten.

Your function should return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.
"""


def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    oranges = []
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            if grid[col][row] == 2:
                oranges.insert(0, (col, row))

    distance_dict = {}
    for orange in oranges:
        distance_dict[orange] = 0
    largest_dist = 0
    while len(oranges) > 0:
        current_orange = oranges.pop()
        current_distance = distance_dict[current_orange]
        if current_distance > largest_dist:
            largest_dist = current_distance
        current_col, current_row = current_orange
        grid[current_col][current_row] = 2

        edge_check = [0, -1, 0, 1]
        print(" ")
        for i in range(len(edge_check)):
            row = current_row + edge_check[i]
            col = current_col + edge_check[(i + 1) % 4]
            print(edge_check[i], edge_check[(i + 1) % 4])
            if col > 0 and col < len(grid) and row >= 0 and row < len(grid[col]) and grid[col][row] == 1:
                cell = (col, row)
                if cell in distance_dict:
                    if distance_dict[cell] < current_distance + 1:
                        distance_dict[cell] = current_distance + 1
                else:
                    distance_dict[cell] = current_distance + 1
                    oranges.insert(0, cell)
    print(grid)
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            if grid[col][row] == 1:
                return -1
    print(largest_dist)
    return largest_dist

    pass


# Test Cases
oranges1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
assert timeToRot(oranges1) == 4

oranges2 = [
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]
assert timeToRot(oranges2) == -1

oranges3 = [
    [0, 2]
]
assert timeToRot(oranges3) == 0
