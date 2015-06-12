NUMBERS = {
    5: 'Five',
    4: 'Four',
    3: 'Three',
    2: 'Two',
    1: 'One',
}


def main():
    for key, value in NUMBERS.iteritems():
        if key == 1:
            print("%s little monkey jumping on the bed" % value)
            print("They fell off and bumped their head")
        else:
            print("%s little monkeys jumping on the bed" % value)
            print("One fell off and bumped their head")

        print("Mama called the doctor")
        print("And the doctor said")

        if key == 1:
            print("Put those monkeys right to bed\n")
        else:
            print("No more monkeys jumping on the bed\n")

if __name__ == "__main__":
    main()
