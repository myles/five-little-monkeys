let numberOfMonkeys: [Int:String] = [
	1: "One",
	2: "Two",
	3: "Three",
	4: "Four",
	5: "Five"
]

let sortedNumberOfMonkeys = numberOfMonkeys.sort {$0.0 > $1.0}

for (index, (key, value)) in sortedNumberOfMonkeys.enumerate() {
	if key == 1 {
		print("\(value) little monkey jumping on the bed")
		print("They fell off and bumped their head")
	} else {
		print("\(value) little monkeys jumping on the bed")
		print("One fell off and bumped their head")
	}
	
	print("Mama called the doctor,")
	print("And the doctor said")
	
	if key == 1 {
		print("Put those monkeys right to bed\n")
	} else {
		print("No more monkeys jumping on the bed\n")
	}
}
