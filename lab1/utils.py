import math


def mean(data_list):
    return sum(data_list) / len(data_list)


def std_dev(data_list):
    std_dev = 0
    m = mean(data_list)
    for num in data_list:
        std_dev += ((num - m) ** 2)

    std_dev /= (len(data_list) - 1)
    std_dev = std_dev ** 0.5

    return std_dev


def median(data_list):
    return n_percentil(data_list, 50)


def n_quartil(data_list, n):
    if n not in [1, 2, 3]:
        raise Exception(
            'N argument must be 1, 2, or 3 for n_quartil operation')

    return n_percentil(data_list, n * 25)


def n_percentil(data_list, n):
    if n is None:
        raise Exception('N argument not optional for n_percentil operation')

    if n < 1 or n > 99:
        raise Exception(
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
