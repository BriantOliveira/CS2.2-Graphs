class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]:  # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else:  # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(1, rows):
        for col in range(1, cols):
            if strA[row - 1] == strB[col - 1]:
                dp_table[row][col] = dp_table[row - 1][col - 1] + 1
            else:
                dp_table[row][col] = max(
                    dp_table[row][col - 1], dp_table[row - 1][col])

    return dp_table[rows-1][cols-1]


def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""

    if not items or not capacity:
        return 0

    value_without = knapsack(items[1:], capacity)
    if(items[0][1] > capacity):
        return value_without
    value_with = knapsack(items[1:], capacity - items[0][1]) + items[0][2]

    return max(value_without, value_with)

    pass


def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(1, rows):
        for col in range(1, cols):
            if row == 0 or col == 0:
                dp_table[row][col] = 0
            elif items[row-1][1] > col:
                dp_table[row][col] = dp_table[row-1][col]
            else:
                value_with = items[row-1][2] + \
                    dp_table[row-1][col - items[row-1][1]]
                value_without = dp_table[row-1][col]
                dp_table[row][col] = max(value_with, value_without)

    return dp_table[rows-1][cols-1]


def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2))
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    insert = edit_distance(str1, str2[:-1])
    delete = edit_distance(str1[:-1], str2)
    replace = edit_distance(str1[:-1], str2[:-1])
    return min(insert, delete, replace) + 1
    pass


def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0:
                dp_table[row][col] = max(row, col)
            else:
                if str1[row - 1] == str2[col - 1]:
                    dp_table[row][col] = dp_table[row - 1][col - 1]
                else:
                    replace = dp_table[row - 1][col - 1]
                    insert = dp_table[row][col - 1]
                    delete = dp_table[row - 1][col]
                    dp_table[row][col] = min(replace, insert, delete) + 1

    return dp_table[rows-1][cols-1]
