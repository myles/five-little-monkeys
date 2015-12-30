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

    def test_rust(self):
        compile_rust = subprocess.check_output([
            'rustc',
            '--out-dir=./tests/tmp/',
            './five-little-monkeys.rs'
        ])
        result = subprocess.check_output([
            './tests/tmp/five-little-monkeys'
        ])
        self.assertMultiLineEqual(result, self.five_little_monkeys)

    def test_scss(self):
        result = subprocess.check_output([
            'sassc',
            'five-little-monkeys.scss'
        ])

        with open('./tests/tmp/five-little-monkeys.html', 'w') as f:
            f.write('<!DOCTYPE html>\n<html>\n<head>\n')
            f.write("<title>Five Little Monkey's</title>\n")
            f.write('<style>\n')
            f.write(result)
            f.write('</style>\n</head>\n<body>\n')
            for stanza in range(1, 6):
                f.write('<div class="stanza stanza-%s">\n' % stanza)
                for line in range(1, 6):
                    f.write('<p class="line line-%s"></p>\n' % line)
                f.write('</div>\n')
            f.write('</body>\n</html>\n')

if __name__ == '__main__':
    unittest.main()
