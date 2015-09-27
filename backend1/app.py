# To-do:
#   1. Write unit tests
#   2. I/O

def jumblesort(line):
    bag = line.split(' ')
    sorted_list = []
    numbers = sorted([int(x) for x in bag if is_digit(x)])
    words = sorted(filter(lambda x: not is_digit(x), bag))

    for item in bag:
        if is_digit(item):
            sorted_list.append(numbers.pop(0))
        else:
            sorted_list.append(words.pop(0))

    jumbled = " ".join(str(item) for item in sorted_list)
    return jumbled

def is_digit(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # testing
    lines = [
        '1',
        'car truck bus',
        '8 4 6 1 -2 9 5',
        'car truck 8 4 bus 6 1'
    ]
    for line in lines:
        print jumblesort(line)
