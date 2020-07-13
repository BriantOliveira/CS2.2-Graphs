"""
Write a function, numIslands, which takes in a 2D grid map of 1s (land) and 0s (water). Your function should return the number of distinct islands in the grid. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    # will contain every seperate island
    islands = []
    # to make sure we have covered all of the land
    all_land = set()
    # keeps track of the nodes that need to be checked on the current island
    needs_check = []
    # adds every land node to the all_land set
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            cell = grid[col][row]
            if cell == 1:
                all_land.add((col, row))

    # makes sure all land is covered
    while all_land:
        # add the first land cell in the all_land set to start the search
        needs_check.append(list(all_land).pop())
        # add a new set to our island which will contain all pieces of land contianed within the newest island
        islands.append(set())
        # loop until all possible connected land has been searched
        while len(needs_check) > 0:
            # grab the newest land from the stack
            current_land = needs_check.pop()
            # if current_land is in all_land, search it, otherwise skip it
            if(current_land in all_land):
                # remove current_land so we know we've searched it
                all_land.remove(current_land)
                # add the current_land to the current island
                islands[-1].add(current_land)
                # deconstruct the tuple to get the row and col of our current_land
                col, row = current_land

                # search the 4 cardinal directions and add them to the stack if they are land
                if col != 0 and grid[col - 1][row] == 1:
                    needs_check.append((col - 1, row))
                if col < len(grid) - 1 and grid[col + 1][row] == 1:
                    needs_check.append((col + 1, row))
                if row != 0 and grid[col][row - 1] == 1:
                    needs_check.append((col, row - 1))
                if row < len(grid[col]) - 1 and grid[col][row + 1] == 1:
                    needs_check.append((col, row + 1))
    return len(islands)

    pass


# Test Cases
map1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
assert numIslands(map1) == 1

map2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
assert numIslands(map2) == 3
