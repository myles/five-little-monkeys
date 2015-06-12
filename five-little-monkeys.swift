var numberOfMonkeys = [
	1: "One",
	2: "Two",
	3: "Three",
	4: "Four",
	5: "Five"
]

let sortedNumberOfMonkeys = Array(numberOfMonkeys.keys).sorted(>)

for (key, value) in enumerate(sortedNumberOfMonkeys) {
	if key == 1 {
		println("\(value) little moneky jumping on the bed")
		println("They fell off and bumped their head")
	} else {
		println("\(value) little monekys jumping on the bed")
		println("One fell off and bumped their head")
	}
	
	println("Mama called the doctor,")
	println("And the doctor said")
	
	if key == 1 {
		println("Put those monkeys right to bed\n")
	} else {
		println("No more monkeys jumping on the bed\n")
	}
}
