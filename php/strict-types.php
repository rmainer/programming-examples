<?php
	declare(strict_types = 1);

	// https://www.php.net/manual/en/functions.arguments.php#functions.arguments.type-declaration.types

	function add(int $x, int $y): int {
		return $x + $y;
	}

	echo add(1,2);
?>