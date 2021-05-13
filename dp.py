def subset_sum_DP(set, target):
    """
    Finds in given set subset whose sum is equal or as close as possible to
    given target. Uses dynamic programming algorithm. Needs set of numbers
    and target value as an input, returns tuple of vars: is sum of subset 
    equal to target, subset sum, subset as list and table.

    :param set: list<int>
    :param target: unsigned int
    :return: tuple (boolean, unsigned int, list, list<list<unsigned int>>])
    """
    n = len(set)

    # fills table n x target with zeroes
    table = [[0 for x in range(target + 1)] for x in range(n + 1)]

    # main part of the algorithm
    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif set[i - 1] <= j:
                table[i][j] = max(
                    set[i - 1] + table[i - 1][j - set[i - 1]],
                    table[i - 1][j]
                )
            else:
                table[i][j] = table[i - 1][j]

    # initalizes vars for getting output subset
    i = n
    j = target
    subset = []

    # gets output subset based on table
    while i > 0 and j > 0:
        if table[i][j] == table[i - 1][j]:
            i = i - 1
        else:
            subset.append(set[i - 1])
            j = j - set[i - 1]
            i = i - 1

    # checks if sum of subset is equal to target
    does_subset_exist = False
    if table[n][target] == target:
        does_subset_exist = True

    return (does_subset_exist, sum(subset), subset, table)