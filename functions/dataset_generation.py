from random import randint

def get_dataset_from_file(filename):
    """
    Loads dataset and target from the csv file. (1st row - dataset, 
    2nd row - target)

    :param filename: string
    :return: tuple (list<int>, int)
    """
    input = open(filename, 'r')
    row = input.readline()
    set = row.split(',')
    set = [int(numeric_string) for numeric_string in set]
    target = input.readline()
    target = int(target)
    input.close()
    return set, target


def generate_set_from_file(filename):
    """
    Loads n, target and boundary, then generates set of n elements.
    Max value of th element is given boundary (if boundary is not given,
    max value is target * 0.5).
    
    :param filename: string
    :return: tuple (list<int>, int)
    """
    input = open(filename, 'r')
    row = input.readline()
    n = int(row)
    row = input.readline()
    target = int(row)
    row = input.readline()
    input.close()
    
    if row:
        boundary = int(row)
    else:
        boundary = int(target * 0.5)
    
    set = [randint(0, boundary) for i in range(n)]

    return set, target

def generate_set(n, target, boundary=None):
    """
    Generates set of n elements. Max value of the element is given 
    boundary (if boundary is not given, max value is target * 0.5).

    :param n: int
    :param target: int
    :paramboundary: int
    :return: tuple (list<int>, int)
    """
    if boundary == None:
        boundary = int(target * 0.5)
    
    set = [randint(0, boundary) for i in range(n)]

    return set, target