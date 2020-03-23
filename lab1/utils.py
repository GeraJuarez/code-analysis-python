import math


def mean(data_list):
    """Calculate the mean of numbers in a list.

    Args:
        data_list: the list of numbers.

    Returns:
        The mean of the list as a float type.
    """

    return sum(data_list) / len(data_list)


def std_dev(data_list):
    """Calculate the standard deviation of numbers in a list.

    Args:
        data_list: the list of numbers.

    Returns:
        The standard deviation of the list as a float type.
    """

    std_dev = 0
    m = mean(data_list)
    for num in data_list:
        std_dev += ((num - m) ** 2)

    std_dev /= (len(data_list) - 1)
    std_dev = std_dev ** 0.5

    return std_dev


def median(data_list):
    """finds the median from a list of numbers.

    Same as calculating the 50th percentil and the 2th quartil.

    Args:
        data_list: the list of numbers.

    Returns:
        The values corresponding to the median.
    """

    return n_percentil(data_list, 50)


def n_quartil(data_list, n):
    """finds the n-th quartil from a list of numbers.

    It calculates the 1st quartil, the 2nd quartil, or the 3rd quartil.

    Args:
        data_list: the list of numbers.
        n: int, the desired quartil (1, 2, 3)

    Returns:
        The specified n-th quartil.

    Raises:
        TypeError
    """

    if n not in [1, 2, 3]:
        raise TypeError(
            'N argument must be 1, 2, or 3 for n_quartil operation')

    return n_percentil(data_list, n * 25)


def n_percentil(data_list, n):
    """finds the n-th percentil from a list of numbers.

    Args:
        data_list: the list of numbers.
        n: int, the desired percentil between 1 and 99.

    Returns:
        The specified n-th quartil.

    Raises:
        TypeError
    """

    if n is None:
        raise TypeError('N argument not optional for n_percentil operation')

    if n < 1 or n > 99:
        raise TypeError(
            'N argument must be between 1 and 99 for n_percentil operation')

    sorted_data = sorted(data_list)
    size = len(sorted_data)
    index = size * n / 100

    if index.is_integer():
        index = int(index - 1)
        return (sorted_data[index] + sorted_data[index + 1]) / 2
    else:
        index = math.ceil(index) - 1
        return sorted_data[index]


if __name__ == "__main__":  # pragma: no cover
    import argparse

    FUNCTION_MAP = {
        'mean': mean,
        'std_dev': std_dev,
        'median': median,
        'n_quartil': n_quartil,
        'n_percentil': n_percentil,
    }

    parser = argparse.ArgumentParser(description='Decimal to Roman Converter')
    parser.add_argument('operation', choices=FUNCTION_MAP.keys())
    parser.add_argument('path', type=str, action='store',
                        help='The path with file of numbers')
    parser.add_argument('-n', type=int, action='store',
                        help='N parameter for quartil and percentil')
    args = parser.parse_args()

    numbers_list = []
    with open(args.path, "r") as fp:
        for line in fp:
            numbers_list.append(int(line))

    func = FUNCTION_MAP[args.operation]
    try:
        if args.operation == 'n_quartil' or args.operation == 'n_percentil':
            print(func(numbers_list, args.n))
        else:
            print(func(numbers_list))
    except Exception as err:
        print(f'Invalid argument: {err}')
