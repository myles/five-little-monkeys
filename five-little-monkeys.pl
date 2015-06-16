use strict;
use warnings;
use 5.010;

my %numbers = (
    1 => 'One',
    2 => 'Two',
    3 => 'Three',
    4 => 'Four',
    5 => 'Five'
);

for my $key ( sort {$b<=>$a} keys %numbers) {
    if ($key == 1) {
        print "$numbers{$key} little monkey jumping on the bed\n";
        print "They fell off and bumped their head\n";
    } else {
        print "$numbers{$key} little monkeys jumping on the bed\n";
        print "One fell off and bumped their head\n";
    }
    
    print "Mama called the doctor,\n";
    print "And the doctor said\n";
    
    if ($key == 1) {
        print "Put those monkeys right to bed\n\n";
    } else {
        print "No more monkeys jumping on the bed\n\n"
    }
}