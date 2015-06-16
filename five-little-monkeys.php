<?php
    $numbers = array(
        1 => "One",
        2 => "Two",
        3 => "Three",
        4 => "Four",
        5 => "Five"
    );
	
	krsort($numbers);
    
    foreach ($numbers as $key => $value) {
        if ($key == 1) {
            print_r($value . " little monkey jumping on the bed\n");
			print_r("They fell off and bumped their head\n");
        } else {
        	print_r($value . " little monkeys jumping on the bed\n");
			print_r("One fell off and bumped their head\n");
        }
		
	    print_r("Mama called the doctor,\n");
	    print_r("And the doctor said\n");
    
	    if ($key == 1) {
	        print_r("Put those monkeys right to bed\n\n");
	    } else {
	        print_r("No more monkeys jumping on the bed\n\n");
	    }
    }
?>