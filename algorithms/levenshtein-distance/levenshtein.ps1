function levenshtein([String]$w1, [String]$w2) {
	$w1 = $w1.ToLower()
	$w2 = $w2.ToLower()
	[Int]$n1 = $w1.Length + 1
	[Int]$n2 = $w2.Length + 1
	$d = New-Object 'Int[,]' $n1,$n2
	
	for ([Int]$y=0; $y -lt $n1; $y++) {
		for ([Int]$x=0; $x -lt $n2; $x++) {
			$d[$y,$x] = 0
		}
	}
	for ([Int]$y=1; $y -lt $n1; $y++) {
		$d[$y,0] = $y
	}
	for ([Int]$x=1; $x -lt $n2; $x++) {
		$d[0,$x] = $x
	}

	for ([Int]$y=1; $y -lt $n1; $y++) {
		for ([Int]$x=1; $x -lt $n2; $x++) {
			if ($w1[$y-1] -eq $w2[$x-1]) {
				$d[$y,$x] = $d[($y-1),($x-1)]
			}
			else {
				$d[$y,$x] = [math]::min(($d[($y-1),($x-1)]) , [math]::min(($d[($y-1),$x]), ($d[$y,($x-1)]))) + 1
			}
		}
	}

	return $d[($y-1),($x-1)]
}

levenshtein "Roman" "Ramon"