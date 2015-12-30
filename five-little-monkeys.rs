fn main() {
	let number_of_monkeys = vec![ "One", "Two", "Three", "Four", "Five" ];
	
	for monkey in number_of_monkeys.iter().rev() {
		if monkey.to_string() == "One" {
			println!("{} little monkey jumping on the bed", monkey);
			println!("They fell off and bumped their head");
		} else {
			println!("{} little monkeys jumping on the bed", monkey);
			println!("One fell off and bumped their head");
		}
		
		println!("Mama called the doctor,");
		println!("And the doctor said");
		
		if monkey.to_string() == "One" {
			println!("Put those monkeys right to bed\n");
		} else {
			println!("No more monkeys jumping on the bed\n");
		}
	}
}