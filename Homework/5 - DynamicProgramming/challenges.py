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

    # Fill in the table using a nested for loop.

    # start at index 1 of dp_table in order to get the diagonal value if i-1 == 0
    # or j-1 == 0 (starting at first character of the string)
    for i in range(1, rows):
        for j in range(1, cols):
            if strA[i-1] == strB[j-1]:
                dp_table[i][j] = 1 + dp_table[i-1][j-1]
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

    return dp_table[rows-1][cols-1]


def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    # item = (name, weight, value)
    if capacity == 0 or len(items) == 0:
        return 0
    name, weight, value = items[0]
    value_with = value + knapsack(items[1:], capacity - weight)
    value_without = knapsack(items[1:], capacity)
    if weight > capacity:
        return value_without
    return max(value_with, value_without)


def knapsack_memoized():
    pass


def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    # item = (name, weight, value)

    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    for i in range(1, rows):
        for capacity in range(1, cols):
            j = i-1  # index of each item starting from 0
            name, weight, value = items[j]
            val_1 = dp_table[i-1][capacity]
            val_2 = dp_table[i-1][capacity - weight] + value
            if capacity - weight < 0:
                dp_table[i][capacity] = val_1
            else:
                dp_table[i][capacity] = max(val_1, val_2)

    return dp_table[rows-1][cols-1]


@Memoize
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2))

    modify = edit_distance(str1[:-1], str2[:-1])

    if str1[-1] == str2[-1]:
        return modify

    insert = edit_distance(str1, str2[:-1])
    delete = edit_distance(str1[:-1], str2)

    return 1 + min(insert, delete, modify)


def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    for r in range(rows):
        for c in range(cols):
            if r == 0 or c == 0:
                dp_table[r][c] = max(r, c)
                continue
            s1 = str1[r-1]
            s2 = str2[c-1]
            modify = dp_table[r-1][c-1]
            if s1 == s2:
                dp_table[r][c] = modify
                continue
            insert = dp_table[r-1][c]
            delete = dp_table[r][c-1]
            dp_table[r][c] = 1 + min(insert, delete, modify)

    return dp_table[-1][-1]
