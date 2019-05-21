<?php
	
	declare(strict_types = 1);

	// ascending
	function insertion_sort_asc(array &$A) : void {
		for($i = 1; $i < count($A); $i++) {
			$j = $i;
			while($j > 0 && $A[$j-1] > $A[$j]) {
				$t = $A[$j];
				$A[$j] = $A[$j-1];
				$A[$j-1] = $t;
				$j--;
			}
		}
	}

	// descending
	function insertion_sort_desc(array &$A) : void {
		for($i = 1; $i < count($A); $i++) {
			$j = $i;
			while($j > 0 && $A[$j-1] < $A[$j]) {
				$t = $A[$j];
				$A[$j] = $A[$j-1];
				$A[$j-1] = $t;
				$j--;
			}
		}
	}

	$A = array(8, 3, 1, 6, 10, 2, 9, 5, 7, 4);
	insertion_sort_asc($A);
	echo "Ascending: "; print_r($A);
	insertion_sort_desc($A);
	echo "Descending: "; print_r($A);

?>