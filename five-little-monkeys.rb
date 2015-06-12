lyrics = "%{number} little monkeys jumping on the bed
One fell off and bumped his head
Mama called the doctor,
And the doctor said
%{last_line}\n
"

last_line = 'No more monkeys jumping on the bed'

last_last_line = 'Put those monkeys right to bed'

(1..5).reverse_each do |x|
  last_line = last_last_line if x == 1

  puts lyrics % { number: x, last_line: last_line }
end
