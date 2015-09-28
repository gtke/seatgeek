import sys
import unittest


class CommandLineInterface(object):
    def read_program_mode(self):
        mode = input('Enter 0 to run JumbleSort. Enter 1 to run unit tests...\n')
        return mode

    def read_input(self):
        line = raw_input('Enter the line (e.g. car truck 8 4 bus 6 1):\n')
        return line


class JumbleSort(object):

    def jumblesort(self, line):
        bag = line.split(' ')
        sorted_list = []
        numbers = sorted([int(x) for x in bag if self.is_digit(x)])
        words = sorted(filter(lambda x: not self.is_digit(x), bag))

        for item in bag:
            if self.is_digit(item):
                sorted_list.append(numbers.pop(0))
            else:
                sorted_list.append(words.pop(0))

        jumbled = " ".join(str(item) for item in sorted_list)
        return jumbled

    def is_digit(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False


class JumbleSortTestCase(unittest.TestCase):

    def setUp(self):
        self.jumble = JumbleSort()

    def test_empty(self):
        line = ''
        expected = ''
        result = self.jumble.jumblesort(line)
        self.assertEquals(expected, result)

    def test_single_character(self):
        line = '1'
        expected = '1'
        result = self.jumble.jumblesort(line)
        self.assertEquals(expected, result)

    def test_only_strings(self):
        line  = 'car truck bus'
        expected = 'bus car truck'
        result = self.jumble.jumblesort(line)
        self.assertEquals(expected, result)

    def test_only_integers(self):
        line = '8 4 6 1 -2 9 5'
        expected = '-2 1 4 5 6 8 9'
        result = self.jumble.jumblesort(line)
        self.assertEquals(expected, result)

    def test_mixed(self):
        line = 'car truck 8 4 bus 6 1'
        expected = 'bus car 1 4 truck 6 8'
        result = self.jumble.jumblesort(line)
        self.assertEquals(expected, result)

    def test_mixed_with_negative_integers(self):
        line = 'car truck -8 4 bus -6 1'
        expected = 'bus car -8 -6 truck 1 4'
        result = self.jumble.jumblesort(line)
        self.assertEquals(expected, result)


if __name__ == '__main__':

    cli = CommandLineInterface()
    mode = cli.read_program_mode()

    jumbler = JumbleSort()

    if mode == 0:
        line = cli.read_input()
        print jumbler.jumblesort(line)
    elif mode == 1:
        unittest.main()
