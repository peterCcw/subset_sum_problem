def subset_sum_BF(set, target, n):
    """
    Finds in given set subset whose sum is equal or as close as possible to
    given target. Uses recursive brute force algorithm. Needs set of numbers,
    target value and size of set as an input, returns tuple of vars:
    is sum of subset equal to target, subset sum, subset as list and table.

    :param set: list<int>
    :param target: unsigned int
    :param n: unsigned int
    :return: tuple (boolean, unsigned int, list)
    """
    if n == 0 or target == 0:
        return False, 0, []

    # if element is bigger than target, it is not considered
    elif set[n - 1] > target:
        return subset_sum_BF(set=set, target=target, n=n-1)

    # comparison of two cases: element included and item excluded,
    # bigger is returned
    else:
        # saving tuples of sum of subset and subset into vars
        included = subset_sum_BF(set=set, target=target-set[n-1], n=n-1)
        excluded = subset_sum_BF(set=set, target=target, n=n-1)

        # choosing bigger sum of elements
        included_sum = set[n - 1] + included[1]
        excluded_sum = excluded[1]

        # initializing output vars
        output_set = []
        output_val = 0
        does_subset_exist = False


        if included_sum >= excluded_sum:
            included[2].append(set[n - 1])
            output_set = included[2]
            output_val = included_sum
        else:
            output_set = excluded[2]
            output_val = excluded_sum

        if output_val == target:
            does_subset_exist = True

        return does_subset_exist, output_val, output_set