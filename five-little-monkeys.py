LYRICS = """%(number)s little monkeys jumping on the bed
One fell off and bumped his head
Mama called the doctor,
And the doctor said
%(last_line)s
"""

LAST_LINE = "No more monkeys jumping on the bed"
LAST_LAST_LINE = "Put those monkeys right to bed"

NUMBERS = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five'
}


def main():
    for x in reversed(range(1, 6)):
        if x == 1:
            last_line = LAST_LAST_LINE
        else:
            last_line = LAST_LINE

        print LYRICS % {'number': NUMBERS[x], 'last_line': last_line}

if __name__ == "__main__":
    main()
