ROMAN_SYMBOL = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}


def decimal_to_roman(decimal_input):
    roman_output = ''

    for key in reversed(list(ROMAN_SYMBOL.keys())):
        quotient = decimal_input // key
        roman_symbol = ROMAN_SYMBOL[key] * quotient
        roman_output += roman_symbol
        decimal_input %= key

    return roman_output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Decimal to Roman Converter')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--decimal', type=int, action='store',
                       help='The decimal to convert to Roman number')
    group.add_argument('-p', '--path', type=str, action='store',
                       help='The path with file of decimal numbers to convert')

    args = parser.parse_args()

    if args.decimal:
        print(decimal_to_roman(args.decimal))

    else:
        with open(args.path, "r") as fp:
            for line in fp:
                out = decimal_to_roman(int(line))
                print(out)
