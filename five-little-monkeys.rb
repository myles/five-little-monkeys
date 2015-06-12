numbers = {
  1 => 'One',
  2 => 'Two',
  3 => 'Three',
  4 => 'Four',
  5 => 'Five'
}

(1..5).reverse_each do |x|
  if x == 1
		puts "#{numbers[x]} little monkey jumping on the bed"
    puts 'They fell off and bumped their head'
  else
		puts "#{numbers[x]} little monkeys jumping on the bed"
    puts 'One fell off and bumped their head'
  end

  puts 'Mama called the doctor,'
  puts 'And the doctor said'

  if x == 1
    puts 'Put those monkeys right to bed', ''
  else
    puts 'No more monkeys jumping on the bed', ''
  end
end
