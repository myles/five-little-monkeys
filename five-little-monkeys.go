package main

import (
	"fmt"
)

func main() {
	var numbers = map[int]string{
		5: "Five",
		4: "Four",
		3: "Three",
		2: "Two",
		1: "One",
	}
	
	for key, value := range numbers {
		fmt.Printf("%s little monkeys jumping on the bed\n", value)
		
		if key == 1 {
			fmt.Println("They fell off and bumped their head")
		} else {
			fmt.Println("One fell off and bumped their head")
		}
		
		fmt.Println("Mama called the doctor,")
		fmt.Println("And the doctor said")
		
		if key == 1 {
			fmt.Println("Put those monkeys right to bed\n")
		} else {
			fmt.Println("No more monkeys jumping on the bed\n")
		}
	}
}
