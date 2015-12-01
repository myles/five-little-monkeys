import os
import unittest
import subprocess


class TestEverything(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        example_output_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'five-little-monkeys.txt'
        )

        with open(example_output_file, 'r') as f:
            self.five_little_monkeys = f.read()

    def test_coffeescript(self):
        result = subprocess.check_output([
            'coffee', 'five-little-monkeys.coffee'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)

    def test_golang(self):
        result = subprocess.check_output([
            'go', 'run', 'five-little-monkeys.go'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)

    def test_nodejs(self):
        result = subprocess.check_output([
            'node', 'five-little-monkeys.js'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)

    def test_php(self):
        result = subprocess.check_output([
            'php',
            'five-little-monkeys.php'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)

    def test_perl(self):
        result = subprocess.check_output([
            'perl',
            'five-little-monkeys.pl'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)

    def test_python(self):
        result = subprocess.check_output([
            'python',
            'five-little-monkeys.py'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)

    def test_ruby(self):
        result = subprocess.check_output([
            'ruby',
            'five-little-monkeys.rb'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)

    def test_swift(self):
        result = subprocess.check_output([
            'swift',
            'five-little-monkeys.swift'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)


if __name__ == '__main__':
    unittest.main()
