<?php
	declare(strict_types = 1);
	
	/*
		there is a buildin method `levenshtein`, see http://docs.php.net/manual/en/function.levenshtein.php
		code here is for the lulz
	*/

	function levenshtein1(string $w1, string $w2) : int {
		$w1 = strtolower($w1);
		$w2 = strtolower($w2);
		$n1 = strlen($w1) + 1;
		$n2 = strlen($w2) + 1;
		$d = array_fill(0, $n1, array_fill(0, $n2, 0));

		for($y=1; $y<$n1; $y++) $d[y][0] = y;
		for($x=1; $x<$n2; $x++) $d[0][x] = x;

		for($y=1; $y<$n1; $y++) {
			for($x=1; $x<$n2; $x++) {
				if($w1[$y-1] ==  $w2[$x-1]) {
					$d[$y][$x] = $d[$y-1][$x-1];
				} else {
					$d[$y][$x] = min($d[$y-1][$x-1], $d[$y-1][$x], $d[$y][$x-1]) + 1;
				}
			}
		}
	
		return $d[$n1-1][$n2-1];
	}

	echo levenshtein1("Roman", "Ramon");
?>
