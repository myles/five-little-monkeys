package main

import (
	"fmt"
	"sort"
)

func main() {
	numbers := make(map[int]string)
	numbers[1] = "One"
	numbers[2] = "Two"
	numbers[3] = "Three"
	numbers[4] = "Four"
	numbers[5] = "Five"

	var keys []int
	for k := range numbers {
		keys = append(keys, k)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(keys)))

	for _, k := range keys {
		if k == 1 {
			fmt.Printf("%s little monkey jumping on the bed\n", numbers[k])
		} else {
			fmt.Printf("%s little monkeys jumping on the bed\n", numbers[k])
		}

		if k == 1 {
			fmt.Println("They fell off and bumped their head")
		} else {
			fmt.Println("One fell off and bumped their head")
		}

		fmt.Println("Mama called the doctor,")
		fmt.Println("And the doctor said")

		if k == 1 {
			fmt.Println("Put those monkeys right to bed\n")
		} else {
			fmt.Println("No more monkeys jumping on the bed\n")
		}
	}
}
